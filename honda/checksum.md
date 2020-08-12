# B-CAN checksum algorithm (where used)
##### Not used on most packets AFAIK

### python3

```
def honda_body_checksum(d, l):
    d = (d >> ((8-l)*8)) # remove padding
    d = (d >> 4)

    s = 0

    while (d is not 0x0): s += (d & 0xF); d = d >> 4;
    s = s & 0xF;

    return s;
```
### c++
```
unsigned int honda_checksum(uint64_t d, int l) {
  d >>= ((8-l)*8); // remove padding
  d >>= 4; // remove checksum

  int s = 0;
  while (d) { s += (d & 0xF); d >>= 4; }
  s &= 0xF;

  return s;
}
```
