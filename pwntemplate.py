#!/usr/bin/env python
from pwn import *
import sys



def exploit(r):
   
    r.interactive()
    return





if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process('')
        print util.proc.pidof(r)
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        pause()
        exploit(r)










