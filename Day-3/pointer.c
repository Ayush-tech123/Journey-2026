#include <stdio.h>

void show(int *p) {
    printf("p = %p\n", p);
    printf("*p = %d\n", *p);
}

int main() {
    int a[3] = {10, 20, 30};
    show(a);
    return 0;
}
