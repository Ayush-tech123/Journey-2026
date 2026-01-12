#include <stdio.h>

struct Student {
    int id;
    char grade;
    float marks;
};

int main() {
    struct Student s1;

    printf("Size of struct: %zu\n", sizeof(s1));
    printf("Size of int: %zu\n", sizeof(int));
    printf("Size of char: %zu\n", sizeof(char));
    printf("Size of float: %zu\n", sizeof(float));

    return 0;
}
