#include <stdio.h>
#include <stdlib.h>

typedef unsigned int uint;
typedef unsigned long long ullong;

uint IdxMin(int *T, uint a, uint b)
{
    int i = a, indexmin = a;

    while (i <= b)
        {
            if (T[i] < T[indexmin])
                indexmin = i;
            i++;
        }
    return indexmin;
}


ullong TriSelection(uint *T, uint n)
{
    int K = 0, ptr = 0;
    while (ptr < n)
    {
        K += n - ptr + 1;
        int min_i = IdxMin(T,ptr,n);
        int tmp = T[ptr];
        T[ptr] = T[min_i];
        T[min_i] = tmp;
        ptr++;
    }
    return K + ptr;
}



int main(int argc, char *argv)
{
    int T[10] = {84,59,48,19,72,68,10,87,15,47};
    printf("%d", TriSelection(T, 10));
    return 0;
}
