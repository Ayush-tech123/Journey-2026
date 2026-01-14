#include <stdio.h>

int main() {
    FILE *f;
    char text[100];

    f = fopen("data.txt", "r");

    if (f == NULL) {
        printf("File could not be opened\n");
        return 1;
    }

    fgets(text, 100, f);
    printf("Read from file: %s", text);

    fclose(f);
    return 0;
}
