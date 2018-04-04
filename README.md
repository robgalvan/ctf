# CTF Solutions and Scripts


### PWN

- [Swamp18](swamp18) (2018-03-29) - Did two challs from SwampCTF one was a fun one, where you must use a format string to leak a libc address and the stack canary. T00manybananas helped me with the format string part.
- [Hackernote](pwnabletw/chall_hacknote) (2018-03-22) - First heap challenge completed. Learned how to leak libc address of main_arena from a small bin. Use that to calculate the address of system and overwrite a function pointer to print out a chunk with system.
- [how2heap](how2heap) (2018-03-12 - cont) - Began the journey to learn heap stuff.
- [DawgCTF](dawgctf) (2018-03-10) - CTF at UMBC. Placed second. Mainly did the RE and PWN challenges. One of of two people to solve the ROP challenge. Practice pays off :)
- [scv](train/scv) (2018-03-09) - x64 bit challenege where you must leak a stack canary. Learned stack canaries start with a null byte to prevent leakage. So we can overwrite the first null byte a "\x0a" (new line). Then leak the rest of it.
- [Pwnabletw - Start & orw](pwnabletw) (2018-03-09) - Shellcoding challenges. One involved writing syscall shellcode. After completing, I read a write up that used pwntools in a new way I have not seen before.
- [pivot64](rop-emporium/pivot64/) (2018-02-27) - Same as pivot32 but need to adapt for 64 bit calling conventions. Learned how to leak 64 bit addresses since it is 6 bytes but u64() requires 8 bytes. 
- [pivot32](rop-emporium/pivot32/) (2018-02-26) - used a gadget to pivot ESP since we can overwrite EIP but we do not control the stack.Call a function from shared lib to populate GOT entry. Used puts to leak GOT entry of function. Calculate address of "win" function also located in shared lib. Call main again to now execute the "win" function.  
- [ropasaurusrex](training/ropasaurusrex/) (2018-02-25) - learned how to use write to leak adresses from memory and how to use read to write to memory. Used both to leak got entries, calculate address of another function in library with leak, change a got entry in binary to another function in library, finally call the function using old functions plt.
- [fluff32](rop-emporium/fluff32/) (2018-02-23) - used non trival ROP gadgets to solve. Example no "mov [eax],edx;ret" gadgets. 
- [write464](rop-emporium/write464/) and [write32](rop-emporium/write432) (2018-02-21) - learned how to use gadgets like "mov [r14],r15" or "mov [eax],edx" to write stuff to pointers in memory. Used this to write "/bin/sh" to memory since system() needs a pointer to string as arg.
- [callme64](rop-emporium/callme64/) (2018-02-18) - called functions using 64 bit calling convention where arguments are now passed through register rather than stack.
- [callme32](rop-emporium/callme32/) (2018-02-18) - Use gadgets to clean stack after calling functions (pop pop ret;).
- [tamu](tamu18/) (2018-02-17) - Simple pwn challenges
- [ret2win](rop-emporium/ret2win64/) (2018-02-10) - Overwrite ret addr with addr of win function.
