#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <sys/reg.h>
#include <sys/ptrace.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <linux/unistd.h>
#include <sys/stat.h> 
#include <fcntl.h>

#define ALLOW_PTRACE "allow_ptrace"

int do_child(int argc, char **argv);
int do_trace(pid_t child);

void allow_ptrace() {
  int fd = open("/proc/flag", O_WRONLY);
  write(fd, ALLOW_PTRACE, sizeof(ALLOW_PTRACE));
}

int main(int argc, char **argv) {
  if (argc < 2) {
    fprintf(stderr, "Usage: %s prog args\n", argv[0]);
    exit(1);
  }

  allow_ptrace();

  pid_t child = fork();
  if (child == 0) {
    return do_child(argc - 1, argv + 1);
  } else {
    return do_trace(child);
  }
}

int do_child(int argc, char **argv) {
  char **args = malloc((argc + 1) * sizeof(char*));
  if (args == NULL) {
    printf("Error: Out of memory\n");
    exit(-1);
  }
  memcpy(args, argv, argc * sizeof(char*));
  args[argc] = NULL;
  ptrace(PTRACE_TRACEME);
  return execvp(args[0], args);
}

int do_trace(pid_t child) {
  int status, syscall, retval;
  waitpid(child, &status, 0);

  while(1) {
    ptrace(PTRACE_SYSCALL, child, 0, 0);
    waitpid(child, &status, 0);
    if (WIFEXITED(status))
      return 1;
    long rax = ptrace(PTRACE_PEEKUSER, child, 8 * ORIG_RAX, NULL);
    switch(rax) {
      case __NR_exit:
      case __NR_read:
      //case __NR_fork:
      case __NR_close:
      case __NR_write:
      case __NR_stat:
      case __NR_fstat:
        break;
      default:
        printf("Not allowed syscall : %ld\n", rax);
        kill(child, SIGKILL);
        exit(-1);
    }
  }
}
