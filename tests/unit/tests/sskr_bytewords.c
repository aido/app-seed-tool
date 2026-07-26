/*
 * ByteWords decoding (BCR-2020-012) is how every SSKR shard the user types
 * becomes bytes, and none of it was covered.
 *
 * bolos_ux_sskr_byteword_to_hex() walks the 256-word list and returns the
 * matching index, or SSKR_WORDLIST_LENGTH / SSKR_BYTEWORD_LENGTH -- that is
 * 256, one past the last valid index -- when nothing matches.
 *
 * Three properties are worth pinning down:
 *   - the mapping is a bijection over the 256 words, so decode(encode(i)) == i;
 *   - the list is in alphabetical order, which the prefix-search helpers rely
 *     on: they stop at the first non-match after a run of matches, so an
 *     unsorted list would silently truncate the suggestions offered to a user;
 *   - what the no-match sentinel actually is, since callers store the result
 *     in a char.
 */

#include <stdarg.h>
#include <stdint.h>
#include <stddef.h>
#include <setjmp.h>
#include <cmocka.h>
#include <string.h>

#include "testutils.h"
#include "sskr/common_sskr.h"
#include "sskr/seed_rom_variables.h"

#define WORD_COUNT (SSKR_WORDLIST_LENGTH / SSKR_BYTEWORD_LENGTH) /* 256 */

static void test_every_index_round_trips(void **state)
{
    (void) state;

    for (unsigned int i = 0; i < WORD_COUNT; i++) {
        unsigned char word[SSKR_BYTEWORD_LENGTH + 1] = {0};

        unsigned int written = bolos_ux_sskr_idx_strcpy(i, word);
        if (written != SSKR_BYTEWORD_LENGTH) {
            fail_msg("idx_strcpy(%u) wrote %u bytes, expected %d", i, written, SSKR_BYTEWORD_LENGTH);
        }

        unsigned int back = bolos_ux_sskr_byteword_to_hex(word);
        if (back != i) {
            fail_msg("'%s' (index %u) decoded back to %u", word, i, back);
        }
    }
}

static void test_wordlist_is_alphabetically_ordered(void **state)
{
    (void) state;

    /* bolos_ux_sskr_get_word_next_letters_starting_with() and
     * get_word_count_starting_with() both break out of the scan once a run of
     * matches ends, which is only correct on a sorted list. */
    for (unsigned int i = 1; i < WORD_COUNT; i++) {
        const unsigned char *prev = SSKR_WORDLIST + (i - 1) * SSKR_BYTEWORD_LENGTH;
        const unsigned char *cur = SSKR_WORDLIST + i * SSKR_BYTEWORD_LENGTH;

        if (memcmp(prev, cur, SSKR_BYTEWORD_LENGTH) >= 0) {
            fail_msg("wordlist not ascending at index %u: '%.4s' then '%.4s'", i, prev, cur);
        }
    }
}

static void test_unknown_word_returns_the_sentinel(void **state)
{
    (void) state;

    unsigned char absent[] = "zzzz";
    unsigned int result = bolos_ux_sskr_byteword_to_hex(absent);

    assert_int_equal(result, WORD_COUNT);

    /* Callers assign this to a char (see sskr_shares_word_add), where 256
     * truncates to 0 -- the same value as the first word in the list. */
    print_message("\n    no-match sentinel is %u; stored in a char it becomes %d\n",
                  result,
                  (char) result);
}

static void test_hex_decode_expands_indices_to_words(void **state)
{
    (void) state;

    /* share_hex_decode() is the inverse direction: byte indices back to a
     * space-separated ByteWords string. */
    unsigned char indices[] = {0, 1, 2};
    unsigned char out[3 * (SSKR_BYTEWORD_LENGTH + 1)] = {0};

    unsigned int written = bolos_ux_sskr_share_hex_decode(indices, sizeof(indices), out, sizeof(out));
    assert_true(written > 0);

    for (unsigned int i = 0; i < sizeof(indices); i++) {
        unsigned char expected[SSKR_BYTEWORD_LENGTH + 1] = {0};
        bolos_ux_sskr_idx_strcpy(indices[i], expected);
        if (memcmp(&out[i * (SSKR_BYTEWORD_LENGTH + 1)], expected, SSKR_BYTEWORD_LENGTH) != 0) {
            fail_msg("word %u: got '%.4s', expected '%s'",
                     i, &out[i * (SSKR_BYTEWORD_LENGTH + 1)], expected);
        }
    }
}

int main(void)
{
    const struct CMUnitTest tests[] = {
        cmocka_unit_test(test_every_index_round_trips),
        cmocka_unit_test(test_wordlist_is_alphabetically_ordered),
        cmocka_unit_test(test_unknown_word_returns_the_sentinel),
        cmocka_unit_test(test_hex_decode_expands_indices_to_words),
    };
    return cmocka_run_group_tests(tests, NULL, NULL);
}
