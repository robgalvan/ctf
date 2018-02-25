#include <stdio.h>

typedef struct {
  char buf[0x100];
  FILE* fp;
} buf_with_fp;

int main() {
  buf_with_fp bwf;
  bwf.fp = stdout;
  fgets(bwf.buf, 0x200, stdin);
  fputs(bwf.buf, bwf.fp);
}
