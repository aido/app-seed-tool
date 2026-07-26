/*******************************************************************************
 *   Ledger Seed Tool application
 *   (c) 2016-2025 Ledger SAS
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 ********************************************************************************/

#pragma once

// SSKR helpers
#include "./seed_rom_variables.h"

// Encode SSKR ByteWord as hex
unsigned int bolos_ux_sskr_byteword_to_hex(unsigned char *byteword);

// Combine hex value SSKR shares into seed
void bolos_ux_sskr_to_seed_convert(const unsigned char *sskr_shares_hex,
                                   unsigned int sskr_shares_hex_length,
                                   unsigned int sskr_shares_count,
                                   const unsigned char *words_buffer,
                                   unsigned int *words_buffer_length,
                                   unsigned char *seed);

// convert seed from BIP39 to SSKR
unsigned int bolos_ux_bip39_to_sskr_convert(unsigned char *bip39_words_buffer,
                                            unsigned int bip39_words_buffer_length,
                                            unsigned int bip39_onboarding_kind,
                                            unsigned int *sskr_group_descriptor,
                                            uint8_t *sskr_share_count,
                                            unsigned char *sskr_words_buffer,
                                            unsigned int *sskr_words_buffer_length);

unsigned int bolos_ux_sskr_hex_check(const unsigned char *sskr_shares_hex,
                                     unsigned int sskr_shares_hex_length,
                                     unsigned int sskr_share_count);

// Combine hex encoded SSKR shares into a secret
unsigned int bolos_ux_sskr_combine(unsigned char *sskr_shares_hex,
                                   unsigned int sskr_shares_hex_length,
                                   unsigned int sskr_shares_count,
                                   unsigned char *output);

// Decode a serialized SSKR share into space separated ByteWords
unsigned int bolos_ux_sskr_share_hex_decode(unsigned char *input,
                                            unsigned int input_len,
                                            unsigned char *output,
                                            unsigned int output_len);

unsigned int bolos_ux_sskr_get_word_idx_starting_with(const unsigned char *prefix,
                                                      const unsigned int prefixlength);
unsigned int bolos_ux_sskr_idx_strcpy(const unsigned int index, unsigned char *buffer);
unsigned int bolos_ux_sskr_get_word_count_starting_with(const unsigned char *prefix,
                                                        const unsigned int prefixlength);
unsigned int bolos_ux_sskr_get_word_next_letters_starting_with(const unsigned char *prefix,
                                                               const unsigned int prefixlength,
                                                               unsigned char *next_letters_buffer);

#if defined(HAVE_NBGL)
size_t bolos_ux_sskr_fill_with_candidates(const unsigned char *startingChars,
                                          const size_t startingCharsLength,
                                          char wordCandidatesBuffer[],
                                          const char *wordIndexorBuffer[]);
uint32_t bolos_ux_sskr_get_keyboard_mask(const unsigned char *prefix,
                                         const unsigned int prefixLength);
#endif
