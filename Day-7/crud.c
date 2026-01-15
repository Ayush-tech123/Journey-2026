#include<stdio.h>
#include<stdlib.h>

struct Teacher{
    int id;
    char name[30];
    int salary;
};

int main(){
    struct Teacher *records = NULL;
    int count = 0;
    
     int choice;

    while(1) {
        printf("\n--- Teacher Record System ---\n");
        printf("1. Add Teacher\n");
        printf("2. View All\n");
        printf("3. Search\n");
        printf("4. Edit\n");
        printf("5. Delete\n");
        printf("6. Exit\n");
        printf("Enter choice: ");

        scanf("%d", &choice);

        switch(choice) {
            case 1:
                printf("Add Teacher selected\n");
                
                records = realloc(records , (count + 1) * sizeof(struct Teacher));

                if(records == NULL){
                    printf("Memory Allocation Failed");
                    return 1;
                }
                printf("Entry No. %d\n", count + 1);
                printf("\nEnter Id : ");
                scanf("%d", &records[count].id);
                printf("\nEnter Name : ");
                scanf("%29s", records[count].name);
                printf("\nEnter Salary : ");
                scanf("%d", &records[count].salary);
                count++;
                break;
            case 2:
                printf("View All selected\n");
                if(count == 0){
                    printf("No available records");
                    break;
                }
                for(int i = 0; i < count; i++){
                    printf("Entry no. %d\n", i + 1);
                    printf("ID : %d\n", records[i].id);
                    printf("Name : %s\n", records[i].name);
                    printf("Salary : %d\n", records[i].salary);
                    printf("----------------------------------");
                }
                break;
            case 3:
                printf("Search selected\n");
              
            if(count == 0){
            printf("No records to search\n");
            break;
            }

            int searchId;
            int found = 0;

                printf("Enter ID to search: ");
                scanf("%d", &searchId);
  
            for(int i = 0; i < count; i++){
            if(records[i].id == searchId){
            printf("Record Found\n");
            printf("ID : %d\n", records[i].id);
            printf("Name : %s\n", records[i].name);
            printf("Salary : %d\n", records[i].salary);
            found = 1;
            break;
        }
    }

            if(!found){
            printf("Record not found\n");
            }
            break;

                break;
            case 4:
                printf("Edit selected\n");
                break;
            case 5:
                printf("Delete selected\n");
                break;
            case 6:
                printf("Exiting...\n");
                return 0;
            default:
                printf("Invalid choice\n");
        }
    }


}