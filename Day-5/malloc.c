#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Teacher {
    int id;
    char name[20];
    int salary;
};

int main() {
    struct Teacher *t;

    t = (struct Teacher*) malloc(sizeof(struct Teacher));

    if(t == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    t->id = 1;
    strcpy(t->name, "Ayush");
    t->salary = 50000;

    printf("ID: %d\n", t->id);
    printf("Name: %s\n", t->name);
    printf("Salary: %d\n", t->salary);

    free(t);

    return 0;
}
