#include <stdio.h>

struct Student {
    int id;
    char grade;
    float marks;
};

int main() {
    struct Student s1;

    printf("Address of s1: %p\n", (void*)&s1);
    printf("Address of id: %p\n", (void*)&s1.id);
    printf("Address of grade: %p\n", (void*)&s1.grade);
    printf("Address of marks: %p\n", (void*)&s1.marks);

    return 0;
}
