#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <dlfcn.h>

int main(int argc, char *argv[])
{
  void *self = dlopen(NULL, RTLD_NOW);

  printf("stack   : %p\n", &argc);
  printf("system(): %p\n", dlsym(self, "system"));
  printf("printf(): %p\n", dlsym(self, "printf"));

  return 0;
}