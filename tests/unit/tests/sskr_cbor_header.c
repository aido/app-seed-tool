/*
 * How bolos_ux_sskr_combine() reads the CBOR byte-string header.
 *
 *     uint8_t sskr_share_len = sskr_shares_hex[3] & 0x1F;
 *     if (sskr_share_len > 23) {
 *         sskr_share_len = sskr_shares_hex[4];
 *     }
 *     ...
 *     ptr_sskr_shares[i] = sskr_shares_hex + ... + 4 + (sskr_share_len > 23);
 *
 * The header is 4 bytes in the short form and 5 in the long one. The offset
 * added on the last line is meant to express that, but it tests
 * sskr_share_len *after* it has been overwritten with the declared length, so
 * it is really asking "is the shard longer than 23 bytes?" rather than "was a
 * long header used?".
 *
 * Those two questions have the same answer for anything this app generates --
 * it only emits the long form when the shard needs 24 bytes or more. They come
 * apart for a shard that uses a long header to declare a small length, which is
 * legal CBOR (just not canonical) and which bolos_ux_sskr_hex_check() does not
 * screen out, since it never compares the declared length to anything.
 *
 * These tests record the behaviour rather than assert a desired one.
 */

#include <stdarg.h>
#include <stdint.h>
#include <stddef.h>
#include <setjmp.h>
#include <cmocka.h>
#include <string.h>

#include "testutils.h"
#include "sskr/common_sskr.h"
#include "sskr/sskr-constants.h"

/* a well-formed 1-of-1 shard body, 5 metadata bytes + a 32-byte value */
#define VALUE_LEN (32)
#define SHARD_LEN (SSKR_METADATA_LENGTH_BYTES + VALUE_LEN) /* 37 -> long form */

static void put_shard(uint8_t *p, uint8_t member_index)
{
    p[0] = 0xAB;
    p[1] = 0xCD;
    p[2] = 0x00; /* one 1-of-1 group */
    p[3] = 0x00; /* group_index 0, member_threshold 1 */
    p[4] = member_index;
    memset(&p[SSKR_METADATA_LENGTH_BYTES], 0x42, VALUE_LEN);
}

/* Long header: tag(3) + 0x58 + one length byte, so the shard starts at 5. */
static void test_long_header_with_a_large_length(void **state)
{
    (void) state;

    uint8_t wire[5 + SHARD_LEN + 4];
    uint8_t out[SSKR_MAX_STRENGTH_BYTES];

    memset(wire, 0, sizeof(wire));
    wire[0] = 0xD9;
    wire[1] = 0x9D;
    wire[2] = 0x75;
    wire[3] = 0x58;       /* one length byte follows */
    wire[4] = SHARD_LEN;  /* 37 */
    put_shard(&wire[5], 0);

    unsigned int len = bolos_ux_sskr_combine(wire, sizeof(wire), 1, out);
    print_message("\n    long header, declared %d: combine returned %u\n", SHARD_LEN, len);
}

/*
 * Long header declaring a length of 20. The header still occupies 5 bytes, but
 * `sskr_share_len > 23` is false by then, so the offset comes out as 4 and the
 * shard is read starting one byte early -- on the length byte itself.
 */
static void test_long_header_with_a_small_length(void **state)
{
    (void) state;

    uint8_t wire[5 + SHARD_LEN + 4];
    uint8_t out[SSKR_MAX_STRENGTH_BYTES];

    memset(wire, 0, sizeof(wire));
    wire[0] = 0xD9;
    wire[1] = 0x9D;
    wire[2] = 0x75;
    wire[3] = 0x58; /* long form ... */
    wire[4] = 20;   /* ... declaring only 20 bytes */
    put_shard(&wire[5], 0);

    unsigned int len = bolos_ux_sskr_combine(wire, sizeof(wire), 1, out);
    print_message("    long header, declared 20:  combine returned %u\n", len);
    print_message("      (header offset used: 4 instead of 5, so the shard is read one byte early)\n");
}

/*
 * Additional info 25..31 do not mean "one length byte follows" in CBOR: 25, 26
 * and 27 introduce 2, 4 and 8 byte lengths, 28..30 are reserved and 31 means
 * indefinite. The code treats every value above 23 the same way.
 */
static void test_additional_info_above_24(void **state)
{
    (void) state;

    const uint8_t infos[] = {0x19, 0x1A, 0x1B, 0x1F}; /* 25, 26, 27, 31 */

    for (unsigned i = 0; i < sizeof(infos); i++) {
        uint8_t wire[5 + SHARD_LEN + 4];
        uint8_t out[SSKR_MAX_STRENGTH_BYTES];

        memset(wire, 0, sizeof(wire));
        wire[0] = 0xD9;
        wire[1] = 0x9D;
        wire[2] = 0x75;
        wire[3] = 0x40 | infos[i];
        wire[4] = SHARD_LEN;
        put_shard(&wire[5], 0);

        unsigned int len = bolos_ux_sskr_combine(wire, sizeof(wire), 1, out);
        print_message("    additional info %2u: combine returned %u\n", infos[i], len);
    }
}

int main(void)
{
    const struct CMUnitTest tests[] = {
        cmocka_unit_test(test_long_header_with_a_large_length),
        cmocka_unit_test(test_long_header_with_a_small_length),
        cmocka_unit_test(test_additional_info_above_24),
    };
    return cmocka_run_group_tests(tests, NULL, NULL);
}
