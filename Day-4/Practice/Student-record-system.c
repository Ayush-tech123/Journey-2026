#include <stdio.h>
#include <string.h>

#define TEACHER_COUNT 3

struct Teacher {
    int id;
    char name[20];
    int salary;
};

void printAll(struct Teacher *teachers, int count);

int main() {
    struct Teacher teachers[TEACHER_COUNT];
    int check;

    for(int i = 0; i < TEACHER_COUNT; i++) {
        while(1) {
            printf("\nEnter the id of the Teacher: ");
            scanf("%d", &teachers[i].id);

            printf("Enter the name of Teacher: ");
            scanf("%19s", teachers[i].name);

            printf("Enter the Salary of the Teacher: ");
            scanf("%d", &teachers[i].salary);

            printf("\nStored ID = %d\n", teachers[i].id);
            printf("Stored Name = %s\n", teachers[i].name);
            printf("Stored Salary = %d\n", teachers[i].salary);

            printf("\nIs this correct?\n1. Yes\n2. No\n");
            scanf("%d", &check);

            if(check == 1) break;
        }
    }

    printAll(teachers, TEACHER_COUNT);
    return 0;
}

void printAll(struct Teacher *teachers, int count) {
    for(int i = 0; i < count; i++) {
        printf("\n------------------------------\n");
        printf("Teacher %d\n", i + 1);
        printf("ID: %d\n", teachers[i].id);
        printf("Name: %s\n", teachers[i].name);
        printf("Salary: %d\n", teachers[i].salary);
    }
}
