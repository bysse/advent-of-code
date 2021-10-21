#ifndef INC_2017_IO_UTIL_H
#define INC_2017_IO_UTIL_H

#include <malloc.h>

typedef struct {
    int size;
    unsigned char *data;
} INPUT;

INPUT *read_input(const char *file, int trim) {
    FILE *fp = fopen(file, "r");
    if (!fp) {
        fprintf(stderr, "Failed to open input file %s\n", file);
        return NULL;
    }
    if (fseek(fp, 0, SEEK_END)) {
        fprintf(stderr, "Failed to find input file size\n");
        fclose(fp);
        return NULL;
    }

    INPUT *input = malloc(sizeof(INPUT));

    const int size = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    input->data = malloc(size);
    input->size = size;

    int bytes_read = fread(input->data, 1, size, fp);

    if (bytes_read != size) {
        fprintf(stderr, "Number of bytes read mismatch the size of the file\n");
        fclose(fp);
        return NULL;
    }

    while (input->size > 0 && input->data[input->size - 1] == '\n') {
        input->size--;
    }

    fclose(fp);
    return input;
}

void free_input(INPUT *input) {
    free(input->data);
    free(input);
}


#endif //INC_2017_IO_UTIL_H
