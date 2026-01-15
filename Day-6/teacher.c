#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct Teacher{
    int id;
    char name[30];
    int salary;
};

int main(){
    struct Teacher *t;

    t = malloc(3 * sizeof(struct Teacher));
    
    if(t == NULL){
        printf("Memory Allocation Failed");
        return 1;
    }

    for(int i = 0; i < 3; i++){
        printf("Entry no. %d\n", i + 1);
        printf("\nEnter ID no : ");
        scanf("%d", &t[i].id);
        printf("\nEnter Name : ");
        scanf("%29s", t[i].name);
        printf("\nEnter Salary : ");
        scanf("%d", &t[i].salary);
        printf("Record Stored Succesfully\n");
        printf("------------------------------\n");
    }

    FILE *f;

    f = fopen("Teacher.txt","w");

    if(f == NULL){
        printf("File Creation/Updation Failed");
        return 1;
    }

    for(int i = 0; i < 3; i++){
        fprintf(f,"Entry No %d\n", i + 1);
        fprintf(f,"Id : %d\n", t[i].id);
        fprintf(f,"Name : %s\n", t[i].name);
        fprintf(f,"Salary : %d\n", t[i].salary);
        fprintf(f,"---------------------------\n");

    }

    fclose(f);

    char c[200];

    f = fopen("Teacher.txt","r");

    if(f == NULL){
        printf("File opening failed");
        return 1;
    }

    while(fgets(c , 200 , f) != NULL){
         printf("%s", c);
    }

    fclose(f);

    free(t);

    return 0;
}