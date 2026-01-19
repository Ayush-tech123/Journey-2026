#include<stdio.h>
#include<string.h>
#include<stdlib.h>

struct Teacher{
    int id;
    char name[30];
    int salary;
};

void addTeacher(struct Teacher **records, int *count);
void viewTeachers(struct Teacher *records, int count);
void searchTeacher(struct Teacher *records, int count);
void editTeacher(struct Teacher *records, int count);
void deleteTeacher(struct Teacher **records, int *count);
void saveToFile(struct Teacher *records, int count);
void loadFromFile(struct Teacher **records, int *count);

int main(){
    struct Teacher *records = NULL;
    int count = 0;
    int choice;
    loadFromFile(&records, &count);

    while(1){
        printf("\n--- Teacher Record System ---\n");
        printf("1. Add\n2. View\n3. Search\n4. Edit\n5. Delete\n6. Exit\n");
        scanf("%d", &choice);

        switch(choice){
            case 1: addTeacher(&records, &count); break;
            case 2: viewTeachers(records, count); break;
            case 3: searchTeacher(records, count); break;
            case 4: editTeacher(records, count); break;
            case 5: deleteTeacher(&records, &count); break;
            case 6: saveToFile(records, count);free(records); return 0;
            default: printf("Invalid choice\n");
        }
    }
}

void addTeacher(struct Teacher **records, int *count){
    *records = realloc(*records, (*count + 1) * sizeof(struct Teacher));

    if(*records == NULL){
        printf("Memory allocation failed\n");
        exit(1);
    }

    printf("Enter ID: ");
    scanf("%d", &(*records)[*count].id);
    getchar();

    printf("Enter Name: ");
    fgets((*records)[*count].name, 30, stdin);
    (*records)[*count].name[strcspn((*records)[*count].name, "\n")] = '\0';

    printf("Enter Salary: ");
    scanf("%d", &(*records)[*count].salary);

    (*count)++;
}

void viewTeachers(struct Teacher *records, int count){
    if(count == 0){
        printf("No records\n");
        return;
    }

    for(int i = 0; i < count; i++){
        printf("\nID: %d\nName: %s\nSalary: %d\n",
               records[i].id,
               records[i].name,
               records[i].salary);
    }
}

void searchTeacher(struct Teacher *records, int count){
    if(count == 0){
        printf("No records\n");
        return;
    }

    int id, found = 0;
    printf("Enter ID: ");
    scanf("%d", &id);

    for(int i = 0; i < count; i++){
        if(records[i].id == id){
            printf("Found: %s, %d\n", records[i].name, records[i].salary);
            found = 1;
            break;
        }
    }

    if(!found) printf("Not found\n");
}

void editTeacher(struct Teacher *records, int count){
    if(count == 0){
        printf("No records\n");
        return;
    }

    int id, found = 0;
    char choice;

    printf("Enter ID to edit: ");
    scanf("%d", &id);

    for(int i = 0; i < count; i++){
        if(records[i].id == id){
            found = 1;
            getchar();

            printf("New Name: ");
            fgets(records[i].name, 30, stdin);
            records[i].name[strcspn(records[i].name, "\n")] = '\0';

            printf("New Salary: ");
            scanf("%d", &records[i].salary);

            printf("Updated\n");
            break;
        }
    }

    if(!found) printf("Not found\n");
}

void deleteTeacher(struct Teacher **records, int *count){
    if(*count == 0){
        printf("No records\n");
        return;
    }

    int id, found = 0;
    printf("Enter ID to delete: ");
    scanf("%d", &id);

    for(int i = 0; i < *count; i++){
        if((*records)[i].id == id){
            found = 1;

            for(int j = i; j < *count - 1; j++){
                (*records)[j] = (*records)[j + 1];
            }

            (*count)--;
            *records = realloc(*records, (*count) * sizeof(struct Teacher));

            printf("Deleted\n");
            break;
        }
    }

    if(!found) printf("Not found\n");
}

void saveToFile(struct Teacher *records, int count){
    FILE *f = fopen("teachers.txt", "w");

    if(f == NULL){
        printf("File open failed\n");
        return;
    }

    for(int i = 0; i < count; i++){
        fprintf(f, "%d\n", records[i].id);
        fprintf(f, "%s\n", records[i].name);
        fprintf(f, "%d\n", records[i].salary);
    }

    fclose(f);
    printf("Data saved successfully\n");
}

void loadFromFile(struct Teacher **records, int *count){
    FILE *f = fopen("teachers.txt", "r");

    if(f == NULL){
        return; // No file yet (first run)
    }

    struct Teacher temp;
    *count = 0;

    while(
        fscanf(f, "%d\n", &temp.id) == 1 &&
        fgets(temp.name, 30, f) &&
        fscanf(f, "%d\n", &temp.salary) == 1
    ){
        temp.name[strcspn(temp.name, "\n")] = '\0';

        *records = realloc(*records, (*count + 1) * sizeof(struct Teacher));
        (*records)[*count] = temp;
        (*count)++;
    }

    fclose(f);
    printf("Data loaded successfully\n");
}
