#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void start(char *src) {
  char buf[0x100];
  strcpy(buf, src);
  return;
}

int main(int argc, char *argv[]) {
  if (argc < 2) {
    exit(-1);
  }
  start(argv[1]);
}
