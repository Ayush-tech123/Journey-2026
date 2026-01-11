#include <stdio.h>

void change(int *p) {
    p[1] = 99;
}

int main() {
    int a[3] = {10, 20, 30};

    change(a);

    printf("%d %d %d\n", a[0], a[1], a[2]);

    return 0;
}
