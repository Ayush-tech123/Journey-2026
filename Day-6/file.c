#include <stdio.h>

int main() {
    FILE *f;

    f = fopen("data.txt", "w");

    if (f == NULL) {
        printf("File could not be opened\n");
        return 1;
    }

    fprintf(f, "Hello from C file handling\n");

    fclose(f);

    return 0;
}
