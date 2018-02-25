#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void start(char *src) {
  char buf[0x100];
  strcpy(buf, src);
  return;
}

int main(int argc, char *argv[], char *envp[])
{
  if (argc < 2) {
    exit(-1);
  }

  /* strip env */
  char **env = envp;
  while (*env != NULL) {
    char *delim = strchr(*env, '=');
    
    *delim = '\0';
    printf("Discarding: %s\n", *env);
    *delim = '=';

    char *end = *env + strlen(*env);
    for (char *iter = *env; iter < end; iter ++) {
      *iter = '\0';
    }
    
    env ++;
  }

  start(argv[1]);
}
