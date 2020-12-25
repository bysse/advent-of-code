#include <stdio.h>
#include <stdlib.h>


void doround(int *link, int size, int index) {
    int pick[] = {0,0,0};

    int lastpick = index;
    for (int i=0;i<3;i++) {
        lastpick = link[lastpick];
        if (lastpick == 0) {
            lastpick = link[0];
        }
        pick[i] = lastpick;
    }

    // relink current
    link[index] = link[lastpick];
    
    int dest = index - 1;
    while (1) {        
        if (dest < 1) {
            dest = size;
        }
        if (pick[0] != dest && pick[1] != dest && pick[2] != dest) {
            break;
        }
        dest--;
    }

    int next = link[dest];
    link[dest] = pick[0];
    link[lastpick] = next;
}

void show(int *link, int size) {
    int index = 0;
    for (int i=0;i<size;i++) {
        printf("%d ", link[index]);
        index = link[index];
    }
    printf("\n");    
}

int main() {
    //398254716
    //int seed[] = {3,8,9,1,2,5,4,6,7};
    int seed[] = {3,9,8, 2, 5, 4, 7, 1, 6};
    int size = 1000000;
    int iter = 10000000;

    int * number = malloc(size * sizeof(int));
    for (int i=0;i<9;i++) {
        number[i] = seed[i];
    }
    for (int i=9;i<size;i++) {
        number[i] = i+1;
    }

    int * link = malloc((size+1) * sizeof(int));
    int prev = 0;
    for (int i=0;i<size;i++) {
        link[prev] = number[i];
        prev = number[i];
    }
    link[prev] = 0;

    int index = link[0];
    for (int i=0;i<iter;i++) {
        //show(link, size);
        doround(link, size, index);
        index = link[index];
    }
    //show(link, size);

    long a = link[1];
    long b = link[a];
    printf("A: %ld * %ld = %ld\n", a, b, a*b);


    free(number);
    free(link);

    return 0;
}