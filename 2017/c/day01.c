#include <stdio.h>

#include "io-util.h"

void partA(INPUT *input) {
    int sum = 0;
    unsigned char *data = input->data;
    int prev = data[input->size - 1];
    for (int i = 0; i < input->size; i++) {
        int ch = data[i];
        if (ch == prev) {
            sum += ch - '0';
        }
        prev = ch;
    }
    printf("A: %d\n", sum);
}

void partB(INPUT *input) {
    int sum = 0;
    unsigned char *data = input->data;
    int delta = input->size >> 1;
    for (int i = 0; i < input->size; i++) {
        int ch = data[i];
        if (ch == data[(i + delta) % input->size]) {
            sum += ch - '0';
        }
    }
    printf("B: %d\n", sum);
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