#include<stdio.h>
#include<stdlib.h>

struct Teacher{
    int id;
    char name[20];
    int salary;
};

void printTeachers(struct Teacher *t);

int main(){
    struct Teacher *teachers;

    teachers = malloc(3 * sizeof(struct Teacher));

    if (teachers == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    for(int i = 0; i <= 2; i++){
        printf("------------------------------------------------------------------------------\n");
        printf("Enter the ID of the Teacher : ");
        scanf("%d", &teachers[i].id);
        printf("Enter the name of the Teacher : ");
        scanf("%19s", teachers[i].name);
        printf("Enter the salary of the Teacher : ");
        scanf("%d", &teachers[i].salary);
        printf("------------------------------------------------------------------------------\n");
    }

    int descision;
    printf("If you want to print all entries press 1 else to exit press 2\n");
    scanf("%d", &descision);

    if(descision == 1){
        printTeachers(teachers);
    }
    else if(descision == 2){
        printf("Thank you for using the program");
    }
    else{
        printf("Invalid Input");
    }

    free(teachers);

    return 0;
}

void printTeachers(struct Teacher *t){
    for(int i = 0; i <= 2; i++){
        printf("------------------------------------------------------------------------------\n");
        printf("Entry No : %d\n", i + 1);
        printf("ID : %d\n", t[i].id);
        printf("Name : %s\n", t[i].name);
        printf("Salary : %d\n", t[i].salary);
        printf("------------------------------------------------------------------------------\n");
    }
}
