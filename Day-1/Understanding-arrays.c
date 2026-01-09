#include <stdio.h>

int main() {
    int arr[5] = {10, 20, 30, 40, 50};
    int *p = arr;

    printf("%d\n", arr[0]);
    printf("%d\n", *arr);
    printf("%d\n", *(arr + 1));
    printf("%d\n", p[2]);
    printf("%d\n", *(p + 3));

    return 0;
}
//Here arr is a stores 5 integers worth of space on the stack and decays into a pointer int*
//Stack memory is intialized and terminated by the compiler whereas heap memory is intialized and terminated by the user.