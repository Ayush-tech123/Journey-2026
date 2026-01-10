#include <stdio.h>

int main() {
    int arr[3] = {10, 20, 30};

    printf("arr+1     = %p\n", arr + 1);
    printf("&arr+1    = %p\n", &arr + 1);
    printf("&arr[0]+1 = %p\n", &arr[0] + 1);

    return 0;
}

