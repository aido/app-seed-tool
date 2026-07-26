/*
 * bolos_ux_sskr_hex_check() is the gate every entered SSKR shard passes
 * through, and it currently has no test coverage at all.
 *
 * It verifies three things: the CBOR tag D9 9D 75, that the first 8 bytes are
 * identical across shards, and a CRC32 over each shard. What it does NOT do is
 * compare the length declared in the CBOR header against the span it actually
 * checks -- that span comes from sskr_shares_hex_length / sskr_shares_count,
 * i.e. from how much the UI collected, not from the header.
 *
 * The last case below pins that down, because bolos_ux_sskr_combine() reads its
 * shard length from that same header and hands it to sskr_deserialize_shard().
 */

#include <stdarg.h>
#include <stdint.h>
#include <stddef.h>
#include <setjmp.h>
#include <cmocka.h>
#include <string.h>

#include "testutils.h"
#include "sskr/common_sskr.h"

extern uint32_t cx_crc32(const void *buf, size_t len);

#define SHARD_LEN   (21) /* 5 metadata + 16 value */
#define CBOR_LEN    (4)  /* tag(3) + short-form header(1) */
#define CRC_LEN     (4)
#define SPAN        (CBOR_LEN + SHARD_LEN + CRC_LEN) /* 29 bytes per shard */
#define SHARDS      (2)

/* Writes one shard in the wire form the app produces, with a correct CRC32
 * stored big-endian over everything that precedes it. */
static void build(uint8_t *p, uint8_t member_index)
{
    memset(p, 0, SPAN);
    p[0] = 0xD9;
    p[1] = 0x9D;
    p[2] = 0x75;                        /* CBOR tag #6.40309 */
    p[3] = 0x40 | (SHARD_LEN & 0x1F);   /* byte string, short form */

    p[CBOR_LEN + 0] = 0xAB;             /* identifier, shared by the backup */
    p[CBOR_LEN + 1] = 0xCD;
    p[CBOR_LEN + 2] = 0x00;             /* one 1-of-1 group */
    p[CBOR_LEN + 3] = 0x01;             /* group_index 0, member_threshold 2 */
    p[CBOR_LEN + 4] = member_index;
    memset(&p[CBOR_LEN + 5], 0x42 + member_index, 16);

    uint32_t crc = __builtin_bswap32(cx_crc32(p, SPAN - CRC_LEN));
    memcpy(&p[SPAN - CRC_LEN], &crc, CRC_LEN);
}

static void build_set(uint8_t buf[SHARDS * SPAN])
{
    for (uint8_t i = 0; i < SHARDS; i++) {
        build(&buf[i * SPAN], i);
    }
}

static unsigned int check(uint8_t buf[SHARDS * SPAN])
{
    return bolos_ux_sskr_hex_check(buf, SHARDS * SPAN, SHARDS);
}

static void test_accepts_a_well_formed_set(void **state)
{
    (void) state;
    uint8_t buf[SHARDS * SPAN];
    build_set(buf);
    assert_int_equal(check(buf), 1);
}

static void test_rejects_a_corrupted_crc(void **state)
{
    (void) state;
    uint8_t buf[SHARDS * SPAN];
    build_set(buf);
    buf[SPAN + SPAN - 1] ^= 0x01; /* flip one bit of the second shard's CRC */
    assert_int_equal(check(buf), 0);
}

static void test_rejects_a_wrong_cbor_tag(void **state)
{
    (void) state;
    uint8_t buf[SHARDS * SPAN];
    build_set(buf);
    buf[1] = 0x9C; /* D9 9C 75 -- tag 40277, not SSKR's 40309 */
    build(buf, 0); /* keep the CRC honest so only the tag is wrong */
    buf[1] = 0x9C;
    uint32_t crc = __builtin_bswap32(cx_crc32(buf, SPAN - CRC_LEN));
    memcpy(&buf[SPAN - CRC_LEN], &crc, CRC_LEN);
    assert_int_equal(check(buf), 0);
}

static void test_rejects_shards_from_different_backups(void **state)
{
    (void) state;
    uint8_t buf[SHARDS * SPAN];
    build_set(buf);
    /* give the second shard another identifier, then re-CRC it so the only
     * thing wrong is that it belongs to a different backup */
    buf[SPAN + CBOR_LEN + 0] = 0x12;
    buf[SPAN + CBOR_LEN + 1] = 0x34;
    uint32_t crc = __builtin_bswap32(cx_crc32(&buf[SPAN], SPAN - CRC_LEN));
    memcpy(&buf[SPAN + SPAN - CRC_LEN], &crc, CRC_LEN);
    assert_int_equal(check(buf), 0);
}

/*
 * The declared length and the actual span disagree, and the CRC is honest.
 *
 * Each shard says "a 200-byte byte string follows" while really occupying 29
 * bytes. Whatever this returns is worth knowing: bolos_ux_sskr_combine() takes
 * its shard length from exactly these header bytes.
 */
static void test_declared_length_is_not_cross_checked(void **state)
{
    (void) state;
    uint8_t buf[SHARDS * SPAN];
    build_set(buf);

    for (uint8_t i = 0; i < SHARDS; i++) {
        uint8_t *p = &buf[i * SPAN];
        p[3] = 0x58; /* byte string, one length byte follows */
        p[4] = 200;  /* ... claiming 200 bytes */
        uint32_t crc = __builtin_bswap32(cx_crc32(p, SPAN - CRC_LEN));
        memcpy(&p[SPAN - CRC_LEN], &crc, CRC_LEN);
    }

    unsigned int result = check(buf);
    print_message("\n    hex_check on a shard whose header claims 200 bytes "
                  "in a 29-byte span: %u\n",
                  result);
    assert_int_equal(result, 1); /* documents the absence of a cross-check */
}

int main(void)
{
    const struct CMUnitTest tests[] = {
        cmocka_unit_test(test_accepts_a_well_formed_set),
        cmocka_unit_test(test_rejects_a_corrupted_crc),
        cmocka_unit_test(test_rejects_a_wrong_cbor_tag),
        cmocka_unit_test(test_rejects_shards_from_different_backups),
        cmocka_unit_test(test_declared_length_is_not_cross_checked),
    };
    return cmocka_run_group_tests(tests, NULL, NULL);
}
