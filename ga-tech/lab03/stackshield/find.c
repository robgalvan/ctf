# include <stdio.h>
# include <stdlib.h>


int main(void)
{
  printf("EG address: 0x%lx\n", getenv("SHELLCODE"));
  return 0;
}
