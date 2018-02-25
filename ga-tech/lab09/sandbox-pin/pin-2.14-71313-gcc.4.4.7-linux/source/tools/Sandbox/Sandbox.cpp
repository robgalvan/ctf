#include "pin.H"
#include <stdint.h>
#include <iostream>
#include <fstream>
#include <sys/syscall.h>
#include <cstdlib>

int activated = 0;

VOID SyscallEntry(THREADID threadIndex, CONTEXT *ctxt, SYSCALL_STANDARD std, VOID *v)
{
  ADDRINT sc_num = PIN_GetSyscallNumber(ctxt, std);
  switch(sc_num) {
    case SYS_read:
      break;
    case SYS_write:
      break;
    case SYS_exit:
      break;
    case SYS_exit_group:
      break;
    case SYS_alarm:
      if(activated)
       exit(-1);
      activated = 1;
      break;
    default:
      if(activated) {
        fprintf(stderr, "Invalid syscall : %lu\n", sc_num);
        exit(-1);
      }
      break;
  }
}

int main(int argc, char *argv[])
{
  int err;

  err = PIN_Init(argc, argv);
  if ( !err )
  {
    PIN_AddSyscallEntryFunction(SyscallEntry, 0LL);
    PIN_StartProgram();
    return 0;
  }
  return 1;
}
