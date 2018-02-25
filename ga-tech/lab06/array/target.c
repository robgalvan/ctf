#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>

#define MAX_ARRAY 10

int array[MAX_ARRAY];

void print() {
    int i;
    printf("[*] Printing all values\n");
    for (i = 0; i < MAX_ARRAY; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

void clear() {
    memset(array, 0, sizeof(array));
}

int get_num() {
    char buf[20];
    fgets(buf, sizeof(buf), stdin);
    return atoi(buf);
}

void change() {
    printf("[*] Give me an index to change\n");
    int index = get_num();
    if (index >= MAX_ARRAY) {
        printf("[*] Failed : index >= 10\n");
        return;
    }

    printf("[*] Value?\n");
    int value = get_num();
    array[index] = value;
}

int main() {
    setvbuf(stdin ,NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    char num[3];
    printf("*** Welcome to array simulator ***");
    while(true) {
        printf("\n[*] Menu\n");
        printf("1. Print\n");
        printf("2. Clear\n");
        printf("3. Change\n");
        printf("4. Exit\n\n");

        switch (get_num()) {
            case 1:
                print();
                break;
            case 2:
                clear();
                break;
            case 3:
                change();
                break;
            case 4:
                printf("Bye\n");
                exit(0);
            default:
                printf("[*] Wrong menu number\n");
        }
    }

}
