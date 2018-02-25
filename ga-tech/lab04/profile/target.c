#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define SIZE 0x200
#define PHONE_NUM_SIZE 0x1c

struct date {
  int year;
  int month;
  int day;
};

struct profile {
  void (*print)(char*);
  char *name;
  struct date birthday;

  char phone_number[PHONE_NUM_SIZE];
  bool sensored;
};

struct profile my;

void stripped_read(char* buf, size_t size) {
  size_t read_bytes;
  if ( (read_bytes = read(0, buf, size)) > 0) {
    if (read_bytes > 0 && buf[read_bytes - 1] == '\n')
      buf[read_bytes - 1] = '\0';
  } 
}

void print_profile() {
  printf("========== My profile ==========\n");
  printf("Name : %s\n", my.name);
  printf("Birthday : %d-%d-%d\n", my.birthday.year,
                                    my.birthday.month,
                                    my.birthday.day);

  if (my.sensored)
    printf("Phone number : CENSORED\n");
  else
    my.print(my.phone_number);
  printf("=================================\n"); 
}

void print_menu() {
  write(1, "1. Print profile\n", 17);
  write(1, "2. Edit name\n", 13);
  write(1, "3. Edit birthday\n", 17);
  write(1, "4. Edit phone number\n", 21);
  write(1, "5. Edit censored\n", 17);
  write(1, "6. Edit all\n", 12);
  write(1, "7. Exit\n", 8);
}

char* get_name() {
  char buf[SIZE];
  printf("[*] What's your name?\n");
  stripped_read(buf, sizeof(buf));
  return strdup(buf);
}

struct date get_birthday() {
  struct date d;
  char buf[10];
  printf("[*] What's your birthday?\n");
  printf("- Year?\n");
  stripped_read(buf, sizeof(buf));
  d.year = atoi(buf);
  printf("- Month?\n");
  stripped_read(buf, sizeof(buf));
  d.month = atoi(buf);
  printf("- Day?\n");
  stripped_read(buf, sizeof(buf));
  d.day = atoi(buf);
  return d;
}

void get_phone_number(char* buf) {
  printf("[*] What's your phone number?\n");
  stripped_read(buf, PHONE_NUM_SIZE);
}

bool get_sensored() {
  char buf[SIZE];
  printf("[*] Sensored? (y/n)\n");

  while (true) {
  stripped_read(buf, sizeof(buf));
  if (buf[0] == 'y')
    return true;
  else if (buf[0] == 'n')
    return false;
  else
    printf("y/n\n");
  }
}

void print_phone_number(char* number) {
  printf("Phone number : %s\n", number);
}

void get_profile() {
  my.name = get_name();
  my.birthday = get_birthday();
  get_phone_number(my.phone_number);
  my.sensored = get_sensored();
  if (my.sensored)
    my.print = NULL;
  else
    my.print = print_phone_number;
}

void edit_all() {
  struct profile p;
  printf("[*] Edit all attributes\n");
  p.name = get_name();
  p.birthday = get_birthday();
  get_phone_number(p.phone_number);
  p.sensored = get_sensored();
  if (!p.sensored)
    p.print = print_phone_number;
  memcpy(&my, &p, sizeof(p));
}

int main() {
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);

  printf("[*] Welcome to profile manager\n");
  get_profile();

  while(true) {
    char menu[2];
    print_menu();
    read(0, menu, sizeof(menu));
    
    switch(menu[0]) {
      case '1':
        print_profile();
        break;
      case '2':
        my.name = get_name();
        break;
      case '3':
        my.birthday = get_birthday();
        break;
      case '4':
        get_phone_number(my.phone_number);
        break;
      case '5':
        my.sensored = get_sensored();
        if (my.print == NULL)
          my.print = print_phone_number;
        break;
      case '6':
        edit_all();
        break;
      case '7':
        exit(-1);
      default:
        printf("Wrong menu\n");
    }
  }
}
