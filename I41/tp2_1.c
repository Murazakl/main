#include <stdio.h>
#include <stdlib.h>

uint Increment(uint * A, unsigned char n, unsigned char b);
uint test(unsigned char n, unsigned char b);

int main() {
    unsigned char n = 7;
    unsigned char b = 10;
    uint A[] = {9, 9, 9,2,9,9,2};
    uint i = Increment(A, n, b);
    uint total = test(30, 2);
    printf("%i\n", i);
    printf("%i\n", total);
    return 0;
}

uint Increment(uint * A, unsigned char n, unsigned char b) {
    uint i = 0;
    while ((i<n) && (A[i] == b-1)){
      A[i] = 0;
      i = i+1;
    }
    if (i<n){
      A[i] = A[i] + 1;
    }
    return i;
}

uint test(unsigned char n, unsigned char b) {
    uint * A = malloc(sizeof(uint) * n);
    uint possibilities = 1;
    for(int i = 0; i < n; i++) {
        possibilities *= b;
        A[i] = 0;
    }

    uint modifications = 0;
    for(int i = 0; i < possibilities; i++)
        modifications += Increment(A, n, b);

    return modifications;
}
