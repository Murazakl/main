#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef unsigned int uint;

uint *genperm(uint n)
{
    int *perm = malloc(n * sizeof(int));
    for(int i = 0; i < n; i++)
    {
        perm[i] = i;
        printf("%6d", perm[i]);
    }
    printf("\n");
    srand(time(NULL));
    for(int i = 0; i<n; i++)
    {
        int index = rand() % n;
        int tmp = perm[i];
        perm[i] = perm[index];
        perm[index] = tmp;
    }
    return perm;
}

int main(int argc, char *argv)
{
    int n = 1000;
    int *perm = genperm(n);
    for(int i = 0; i < n; i++)
        printf("%6d", perm[i]);
    return 0;
}
