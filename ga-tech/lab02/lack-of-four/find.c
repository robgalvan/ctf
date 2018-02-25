#include <unistd.h>
 
int main(void)
{
  printf("EG address: 0x%lx\n", getenv("EG"));
  return 0;
}
