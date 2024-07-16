/*******************************************************************************
 *   (c) 2016-2022 Ledger SAS
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

#if defined(TARGET_STAX)

#define memzero(...) explicit_bzero(__VA_ARGS__)

// 16 shares * 229 chars per share (46 SSKR ByteWords)
#define SSKR_SHARES_MAX_LENGTH 3664

/*
 * Sets the number of SSKR shares
 */
void sskr_sharenum_set(const uint8_t sharenum);

/*
 * Returns the SSKR shares
 */
uint8_t sskr_sharenum_get(void);

/*
 * Sets the SSKR threshold
 */
void sskr_threshold_set(const uint8_t threshold);

/*
 * Returns the SSKR threshold
 */
uint8_t sskr_threshold_get(void);

/*
 * Returns the SSKR share count
 */

uint8_t sskr_sharecount_get(void);

/*
 * Erase all information and reset the indexes
 */
void sskr_shares_reset(void);

/*
 * Generate SSKR shares from BIP39 mnemonic
 */
void sskr_shares_from_bip39_mnemonic(void);

/*
 * Returns the generated SSKR shares
 */
char* sskr_shares_get(void);

/*
 * Returns the length of the SSKR shares buffer
 */
size_t sskr_shares_length_get(void);

#endif  // TARGET_STAX