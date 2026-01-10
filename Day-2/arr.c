#include <stdio.h>

int main() {
    int arr[3] = {10, 20, 30};

    printf("arr      = %p\n", arr);
    printf("&arr     = %p\n", &arr);
    printf("&arr[0]  = %p\n", &arr[0]);

    return 0;
}

/*

1) arr represents the address of the first element of the array when used in an expression like printf
   Type: int* it decays to it

2) &arr is a pointer to the entire array of 3 integers
   Type: int (*)[3]

3) &arr[0] is the address of the first element of the array
   Type: int*

*/