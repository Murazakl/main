#include <stdio.h>
#include <stdlib.h>

typedef unsigned int uint;

void Echanger(int *T, uint a, uint b)
{
    int tmp = T[a];
    T[a] = T[b];
    T[b] = tmp;
}


void Tamiser(int *T, uint i, uint n)
{
    uint ifils = 2 * i;
    if ((ifils < n) && (T[ifils+1] > T[ifils]))
        ifils++;
    if ((ifils <= n) && (T[i] < T[ifils]))
    {
        Echanger(T, i, ifils);
        Tamiser(T, ifils, n);
    }
}

void Entasser(int *T, uint n)
{
    uint i = n / 2;
    while (i > 0)
    {
        Tamiser(T, i, n);
        i--;
    }
}

void TriTas(int *T, uint n)
{
    uint k;

    Entasser(T, n);
    k = n;
    while (k > 0)
    {
        Echanger(T, 1, k);
        Tamiser(T, 1, k-1);
        k--;
    }
    for(int j=0; j < n; j++)
        printf("%3d", T[j]);
}

int main(int argc, char *argv)
{
    int n = 14;
    int T[14] = {2,10,9,8,3,7,10,4,3,5,6,11,12,1};

    TriTas(T, n);

    return 0;
}
