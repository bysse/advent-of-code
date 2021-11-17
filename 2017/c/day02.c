#include <stdio.h>
#include <stdlib.h>
#include "io-util.h"

void partA(INPUT *input) {
    unsigned char *data = input->data;
    const int size = input->size;

    int sum = 0, start = 0, min = -1, max = -1;
    for (int i = 0; i < size; i++) {
        int newline = data[i] == '\n';
        if (data[i] == ' ' || data[i] == '\t' || newline) {
            data[i] = 0;
            int value = atoi((const char *) &data[start]);
            start = i + 1;

            if (min < 0) {
                min = value;
                max = value;
            } else {
                if (value < min) min = value;
                if (value > max) max = value;
            }
        }
        if (newline) {
            sum += max - min;
            min = -1;
            max = -1;
            start = i + 1;
            data[i] = '\n';
        }
    }

    // last row
    sum += max - min;

    printf("A: %d\n", sum);
}

int do_div(int *num, int num_count) {
    for (int j = 0; j < num_count; j++) {
        for (int k = 0; k < num_count; k++) {
            if (j == k) continue;
            if (num[j] % num[k] == 0) {
                return num[j] / num[k];
            }
        }
    }
    return -1;
}

void partB(INPUT *input) {
    unsigned char *data = input->data;
    const int size = input->size;

    int *num = (int *) malloc(sizeof(int) * 256);
    int num_count = 0;

    int sum = 0, start = 0;
    for (int i = 0; i < size; i++) {
        int newline = data[i] == '\n';
        if (data[i] == 0 || newline) {
            data[i] = 0;
            num[num_count++] = atoi((const char *) &data[start]);
            start = i + 1;

        }
        if (newline) {

            sum += do_div(num, num_count);
            num_count = 0;
        }
    }

    printf("B: %d\n", sum);
    free(num);
}

int main() {
    INPUT *input = read_input("../input-02.txt", 1);
    if (input == NULL) {
        return 1;
    }

    partA(input);
    partB(input);

    free_input(input);
    return 0;
}