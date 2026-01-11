#include<stdio.h>

void printSize(int arr[]) {
    printf("%zu\n", sizeof(arr));
}

int main() {
    int a[10];
    printSize(a);
}
