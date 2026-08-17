#include <stdio.h>

int main(void) {

    unsigned int a = 0;
    unsigned int b = a - 2;

    printf("%%d: %d\n", b);
    printf("%%u: %u\n", b);

    return 0;
}
