#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned int uint;

uint *Addition(uint *A, uint *B, uint base)
{
    int size_A = 3, size_B = 3;
    if (B > A)
    {
        int *tmp = A;
        A = B;
        B = tmp;
        int tmp_s = size_A;
        size_A = size_B;
        size_B = tmp_s;
    }

    uint *C = malloc((size_A + 1) *sizeof(uint));
    for(int i = 0; i < size_A+1; i++)
        C[i] = 0;

    int i = 0, retenue = 0;
    while (i < size_B)
    {
        C[i] = A[i] + B[i] + retenue;
        if (C[i] >= base)
        {
            retenue = 1;
            C[i] -= base;
        }
        else retenue = 0;
        i++;
    }
    while (i < size_A)
    {
        C[i] = A[i] + retenue;
        if (C[i] >= base)
        {
            retenue = 1;
            C[i] -= base;
        }
        else retenue = 0;
        i++;
    }
    if (retenue > 0) C[i] = retenue;
    return C;
}

uint *Multiplication(uint *A, uint *B, uint base)
{
    int size_A = 3, size_B = 3;
    uint *C = malloc(size_A + size_B * sizeof(uint));
    int i = 0;

    while (i < size_A)
    {
        int retenue = 0, j = 0;
        while (j < size_B)
        {
            C[i+j] += A[i] * B[j] + retenue;
            retenue = C[i+j] / base;
            C[i+j] %= base;
            j++;
        }
        if (retenue > 0) C[i+j] = retenue;
        i++;
    }
    return C;
}
int main(int argc, char *argv)
{
    uint A[3] = {0,2,5};
    uint B[3] = {3,2,4};

    uint *result = Addition(A,B,10);
    uint *result2 = Multiplication(A,B,10);
    for(int i=0; i < 5; i++)
    {
        printf("%d\n", result[i]);
    }
    return 0;
}
