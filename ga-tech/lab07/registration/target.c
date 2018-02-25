#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct _student {
    int gtid;
    char* name;
    struct _student* next;
    char* nickname;
} student;

student* list = NULL;

student* new_student(int gtid, char* name) {
    student* new = (student*) malloc(sizeof(student));
    new->name = name;
    new->gtid = gtid;
    new->next = NULL;
    new->nickname = NULL;
    return new;
}

int get_num() {
    char num[11];
    fgets(num, sizeof(num), stdin);
    return atoi(num);
}

student* get_student() {
    printf("- Give me an index to choose\n");
    int i = 0;
    student* ptr = list;
    int index = get_num();

    for (i = 0; i < index && ptr != NULL; i++) {
        ptr = ptr->next;
    }

    if (ptr == NULL) {
        printf("- No such student\n");
        return NULL;
    }
    return ptr;
}

student* register_course() {
    char buf[0x100];
    printf("[*] Register course!\n");
    printf("- Name?\n");
    fgets(buf, sizeof(buf), stdin);
    buf[strlen(buf) - 1] = 0;

    printf("- GTID?\n");

    student* new = new_student(get_num(), strdup(buf));

    if (list == NULL) {
        list = new;
    }
    else {
        student* ptr = list;
        while (ptr->next) ptr = ptr->next;
        ptr->next = new;
    }

    printf("- Successfully added\n");
}

void print_all() {
    student* ptr;
    int i;
    printf("[*] Print all registered students\n");
    for (i = 0, ptr = list; ptr; i++, ptr = ptr->next) {
        printf("%d. name : %s, gtid : %d", i, ptr->name, ptr->gtid);
        if (ptr->nickname)
            printf(", nickname : %s", ptr->nickname);
        printf("\n");
    }
    printf("-------------------------------------\n");
}

bool yes_or_no() {
    char buf[3];
    while(true) {
        fgets(buf, sizeof(buf), stdin);
        if (buf[0] == 'y')
            return true;
        else if(buf[0] == 'n')
            return false;
        else
            printf("y/n\n");
    }
}

void unregister_course() {
    printf("[*] Unregister course :(\n");
    student* ptr = get_student();
    student* prev = list;
    if (!ptr) return;

    if (ptr != list) {
        while (prev->next != ptr) {
            prev = prev->next;
        }
        prev->next = ptr->next;
    }
    if (ptr->nickname)
        free(ptr->nickname);
    free(ptr->name);
    free(ptr);

    printf("- I think it's not good idea to unregister this course\n");
}

void modify() {
    student* ptr = get_student();
    if (!ptr) return;
    printf("- Wish to change name?(y/n)\n");

    if (yes_or_no()) {
        char buf[0x100];
        printf("- Name?\n");
        fgets(buf, sizeof(buf), stdin);
        buf[strlen(buf) - 1] = 0;

        free(ptr->name);
        ptr->name = strdup(buf);
    }

    printf("- Wish to change gtid?(y/n)\n");

    if (yes_or_no()) {
        char gtid[11];
        printf("- GTID?\n");
        fgets(gtid, sizeof(gtid), stdin);
        ptr->gtid = atoi(gtid);
    }

    printf("- Wish to change nickname?(y/n)\n");

    if (yes_or_no()) {
        char buf[0x100];
        printf("- Nickname?\n");
        fgets(buf, sizeof(buf), stdin);
        buf[strlen(buf) - 1] = 0;

        if (ptr->nickname)
            free(ptr->nickname);
        ptr->nickname = strdup(buf);
    }
}

int main() {
    setvbuf(stdin ,NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    printf("*** Welcome to Course Registration(CS6265) ***\n");
    char num[3];

    while(1) {
        printf("\n1. Register course\n");
        printf("2. Unregister course\n");
        printf("3. Modify student information\n");
        printf("4. Print all registered students\n");
        printf("5. Exit\n\n");
        fgets(num, sizeof(num), stdin);
        switch(atoi(num)) {
            case 1:
                register_course();
                break;
            case 2:
                unregister_course();
                break;
            case 3:
                modify();
                break;
            case 4:
                print_all();
                break;
            case 5:
                exit(0);
        }
    }
}
