#include<stdio.h>
#include<stdlib.h>
#include <string.h>


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
            records = realloc(records, (count + 1) * sizeof(struct Teacher));

             if(records == NULL){
             printf("Memory Allocation Failed");
             return 1;
             }

             printf("Entry No. %d\n", count + 1);

             printf("Enter Id: ");
             scanf("%d", &records[count].id);

             getchar(); 

             printf("Enter Full Name: ");
             fgets(records[count].name, 30, stdin);
             records[count].name[strcspn(records[count].name, "\n")] = '\0';

             printf("Enter Salary: ");
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

                
            case 4:
                printf("Edit selected\n");

            if(count == 0){
                printf("No Record Stored");
                break;
            }

            int searchID;
            char confirm;
            int entry = 0;

            printf("Enter Id to Edit: ");
            scanf("%d", &searchID);
            for(int i = 0; i < count; i++){
                if(records[i].id == searchID){
                    printf("Record found\n");
                    printf("ID : %d\n", records[i].id);
                    printf("Name : %s\n", records[i].name);
                    printf("Salary : %d\n", records[i].salary); 
                    printf("Is this the Record you want to edit (Y/N)\n");
                    getchar();
                    scanf("%c", &confirm);

                    if(confirm == 'Y' || confirm == 'y'){

                        printf("Give the new Entry\n");
                        printf("Enter ID : ");
                        scanf("%d", &records[i].id);
                        getchar(); 

                        printf("Enter Full Name: ");
                        fgets(records[i].name, 30, stdin);
                        records[i].name[strcspn(records[i].name, "\n")] = '\0';
                        printf("\nEnter Salary : ");
                        scanf("%d", &records[i].salary);
                        printf("\nEntry Stored\n");
                        entry = 1;
                        break;
                    }
                    else{
                        continue;
                    }
                }
                
                
            }
           
            if(!entry){
            printf("No Record Found\n");
            break;
                }                
            break;
            case 5:

                printf("Delete selected\n");

                int SearchId;
                char Delete;
                int missing = 0;
                printf("Enter Id to delete: ");
                scanf("%d", &SearchId);

                for(int i = 0; i < count; i++){
                if(records[i].id == SearchId){
                    printf("Record found\n");
                    printf("ID : %d\n", records[i].id);
                    printf("Name : %s\n", records[i].name);
                    printf("Salary : %d\n", records[i].salary); 
                    printf("Is this the Record you want to delete (Y/N)\n");
                    getchar();
                    scanf("%c", &Delete);
                    if(Delete == 'Y' || Delete == 'y'){
                        for(int j = i; j < count - 1; j++){
                            records[j] = records[j + 1];
                        }
                        count--;
                        records = realloc(records, count * sizeof(struct Teacher));
                        printf("Record Deleted Succesfully");
                        break;
                        missing = 1;
                    }
                    else{
                        continue;
                    }    
                }
            }
            if(!missing){
                printf("No record found");
                break;
            }
            break;
            case 6:
                printf("Exiting...\n");
                return 0;
            default:
                printf("Invalid choice\n");
        }
    }


}