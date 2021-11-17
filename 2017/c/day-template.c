#include <stdio.h>
#include "io-util.h"

void partA(INPUT *input) {
}

void partB(INPUT *input) {
}

int main() {
    INPUT *input = read_input("../input-01.txt", 1);
    if (input == NULL) {
        return 1;
    }

    partA(input);
    partB(input);

    free_input(input);
    return 0;
}