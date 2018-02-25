# include <stdio.h>
int main(void)
{
  printf("EG address: 0x%x\n", getenv("SHELLCODE"));
  return 0;
}
