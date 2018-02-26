# CTF Solutions and Scripts

## Challenges Completed

- [pivot32](rop-emporium/pivot32/) (2/26/18) - used a gadget to pivot ESP since we can overwrite EIP but we do not control the stack.Call a function from shared lib to populate GOT entry. Used puts to leak GOT entry of function. Calculate address of "win" function also located in shared lib. Call main again to now execute the "win" function.  
- [ropasaurusrex](train/ropasaurusrex/) (2/25/18) - learned how to use write to leak adresses from memory and how to use read to write to memory. Used both to leak got entries, calculate address of another function in library with leak, change a got entry in binary to another function in library, finally call the function using old functions plt.
- [fluff32](rop-emporium/fluff32/) (2/23/18) - used non trival ROP gadgets to solve. Example no "mov [eax],edx;ret" gadgets. 
- [write464 and write462](rop-emporium/write464/) (2/21/18) - learned how to use gadgets like "mov [r14],r15" or "mov [eax],edx" to write stuff to pointers in memory. Used this to write "/bin/sh" to memory since system() needs a pointer to string as arg.
- [callme64](rop-emporium/callme64/) (2/20/18) - called functions using 64 bit calling convention where arguments are now passed through register rather than stack
- [callme32](rop-emporium/callme32/) (2/20/18) - Use gadgets to clean stack after calling functions (pop pop ret;)


