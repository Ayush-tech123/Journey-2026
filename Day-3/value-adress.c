#include <stdio.h>

void changeValue(int x) {
    x = 50;
}

void changeArray(int *p) {
    p[0] = 50;
}

int main() {
    int a = 10;
    int arr[3] = {10, 20, 30};

    changeValue(a);
    changeArray(arr);

    printf("a = %d\n", a);
    printf("arr[0] = %d\n", arr[0]);

    return 0;
}
