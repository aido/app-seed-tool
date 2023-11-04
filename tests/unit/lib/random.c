#include <stdint.h>
#include <stddef.h>

unsigned char *fake_rng(uint8_t *buffer, size_t len)
{
    for (size_t i = 0; i < len; i++) {
       buffer[i] = i % 256; 
    } 
    return buffer;
}
