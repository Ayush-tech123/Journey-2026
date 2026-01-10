#include <stdio.h>

int main() {
    char a[] = "cat";
    char *b = "dog";

    a[0] = 'C';
    b[0] = 'D';

    printf("a = %s\n", a);
    printf("b = %s\n", b);

    return 0;
}
