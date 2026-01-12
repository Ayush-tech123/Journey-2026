#include <stdio.h>

struct Student {
    int id;
    char grade;
    float marks;
};

int main() {
    struct Student s1;

    s1.id = 101;
    s1.grade = 'A';
    s1.marks = 89.5;

    printf("ID: %d\n", s1.id);
    printf("Grade: %c\n", s1.grade);
    printf("Marks: %.2f\n", s1.marks);

    return 0;
}
