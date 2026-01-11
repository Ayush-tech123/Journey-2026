#include <stdio.h>

void check(int arr[]) {
    printf("Inside function: %zu\n", sizeof(arr));
}

int main() {
    int a[5] = {1,2,3,4,5};
    printf("In main: %zu\n", sizeof(a));
    check(a);
    return 0;
}
