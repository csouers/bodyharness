def honda_body_checksum(d, l):
    d = (d >> ((8-l)*8)) # remove padding
    d = (d >> 4)

    s = 0

    while (d > 0x0): s += (d & 0xF); d = d >> 4;
    s = s & 0xF;

    return s;
