#include "stdio.h"

int main(void) {
    for (int i = 1000; i > 0; i -= 7) {
        printf("%d - 7 = %d\n", i, i - 7);
    }
    printf("I'm a ghoul.\n");
    return 0;
}