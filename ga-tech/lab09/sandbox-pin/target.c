#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>

int main() {
  char buf[1024];
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);

  printf("Activate sandbox...\n");
  alarm(0);

  while(true) {
    if (!fgets(buf, sizeof(buf), stdin))
      break;
    if (!strcmp(buf, "exit\n"))
      break;
    printf(buf);
  }
}
