#include <sys/syscall.h>

.globl main
.type  main, @function

main:
  xorl    %ebx,%ebx
  movl    %ebx,%eax
  inc     %eax
  int     $0x80
