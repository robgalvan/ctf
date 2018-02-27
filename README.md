# CTF Solutions and Scripts


### PWN

- [pivot64](rop-emporium/pivot64/) (2/27/18) - Same as pivot32 but need to adapt for 64 bit calling conventions. Learned how to leak 64 bit addresses since it is 6 bytes but u64() requires 8 bytes. 
- [pivot32](rop-emporium/pivot32/) (2/26/18) - used a gadget to pivot ESP since we can overwrite EIP but we do not control the stack.Call a function from shared lib to populate GOT entry. Used puts to leak GOT entry of function. Calculate address of "win" function also located in shared lib. Call main again to now execute the "win" function.  
- [ropasaurusrex](train/ropasaurusrex/) (2/25/18) - learned how to use write to leak adresses from memory and how to use read to write to memory. Used both to leak got entries, calculate address of another function in library with leak, change a got entry in binary to another function in library, finally call the function using old functions plt.
- [fluff32](rop-emporium/fluff32/) (2/23/18) - used non trival ROP gadgets to solve. Example no "mov [eax],edx;ret" gadgets. 
- [write464](rop-emporium/write464/) and [write32](rop-emporium/write432) (2/21/18) - learned how to use gadgets like "mov [r14],r15" or "mov [eax],edx" to write stuff to pointers in memory. Used this to write "/bin/sh" to memory since system() needs a pointer to string as arg.
- [callme64](rop-emporium/callme64/) (2/20/18) - called functions using 64 bit calling convention where arguments are now passed through register rather than stack.
- [callme32](rop-emporium/callme32/) (2/20/18) - Use gadgets to clean stack after calling functions (pop pop ret;).
- [tamu](tamu18/) (2/17/18) - Simple pwn challenges
- [ret2win](rop-emporium/ret2win64/) (2/10/18) - Overwrite ret addr with addr of win function.


