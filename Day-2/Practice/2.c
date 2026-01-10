#include <stdio.h>

int main() {
    char name[6];

    printf("Enter name: ");
    scanf("%5s", name);

    printf("Stored name: %s\n", name);

    return 0;
}
