#include <stdio.h>

int main() {
    char s1[] = "hello";
    char *s2 = "hello";

    s1[0] = 'H';
    s2[0] = 'H';   // This line is dangerous

    printf("s1 = %s\n", s1);
    printf("s2 = %s\n", s2);

    return 0;
}
