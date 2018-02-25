#include <sys/syscall.h>

.globl main
.type  main, @function

main:
  xorq    %rsi,%rsi               /* arg 2: 0 */
  movq    %rsi,%rax               
  inc     %rax                    /* arg 1: SYS_exit */
  syscall                         /* exit(0) */
