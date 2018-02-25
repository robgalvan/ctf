#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define SIZE 256 

void* container[SIZE];

int read_int() {
  char buf[10];
  fgets(buf, sizeof(buf), stdin);
  return atoi(buf);
}

void allocate() {
  int index;
  for (index = 0; index < SIZE; index++) {
    if (container[index] == NULL)
      break;
  }

  if (index == SIZE) {
    printf("No available storage\n");
    return;
  }

  printf("Memory size?\n");

  int size = read_int();
  container[index] = malloc(size);

  if (container[index] == NULL)
    printf("Error : Out of memory\n");
  else
    printf("Success : Index %d\n", index);
}

void deallocate() {
  printf("Index to free?\n");
  int index = read_int();

  if (container[index] == NULL) 
    printf("Error : Not allocated index\n");
  else
  {
    free(container[index]);
    container[index] = NULL;
    printf("Success\n");
  }
}

void write_to_storage() {
  printf("Index to write?\n");
  int index = read_int();

  if (container[index] == NULL) {
    printf("Error : Not allocated\n");
    return;
  }

  printf("Data size?\n");
  int size = read_int();
  char* memory = container[index];

  printf("Data?\n");
  int ssize = read(0, memory, size);
  if (ssize < 0) {
    printf("Error : read\n");
  }
  else {
    printf("Success\n");
  }
}

void read_from_storage() {
  printf("Index to read?\n");
  int index = read_int();

  if (container[index] == NULL) {
    printf("Error : Not allocated\n");
    return;
  }

  printf("Data : ");
  printf("%s\n", (char*)container[index]);
  printf("\n");
}

int main() {
  setvbuf(stdin ,NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);

  printf("Welcome to Storage\n");

  while(true) {
    printf("\n1. Allocate\n2. Deallocate\n3. Write to storage\n"
        "4. Read from storage\n5. Exit\n");
    switch(read_int()) {

      case 1:
        allocate();
        break;
      case 2:
        deallocate();
        break;
      case 3:
        write_to_storage();
        break;
      case 4:
        printf("Not implemented yet..\n");
        break;
        //read_from_storage();
        break;
      case 5:
        printf("Bye\n");
        return 0;
    }
  }
}
