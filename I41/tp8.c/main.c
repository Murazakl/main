#include <stdio.h>
#include <stdlib.h>

typedef struct {
    uint n;
    int *values;
}   t_liste;

void Copier(t_liste X, uint i, t_liste Y, uint j, uint n)
{
    int k = 0;
    while (k < n)
    {
        Y.values[j+k] = X.values[i+k];
        k++;
    }
}

void Fusionner(t_liste L, uint p, uint q, uint r)
{
    int i, j, k, ng = q-p, nd = r-q;
    t_liste G = {ng, malloc(ng * sizeof(int))};
    t_liste D = {nd, malloc(nd * sizeof(int))};

    Copier(L, p, G, 0, ng);
    Copier(L, q, D, 0, nd);

    i = 0;
    j = 0;
    k = p;

    while ((i < ng && j < nd))
    {
        if (G.values[i] <= D.values[j])
            L.values[k] = G.values[i++];
        else
            L.values[k] = D.values[j++];
        k++;
    }

    free(G.values);
    free(D.values);
}

void TriFusion(t_liste L, uint p, uint r)
{
    uint q;

    if (p < r)
    {
        q = (p+r) / 2;
        TriFusion(L, p, q);
        TriFusion(L, q+1, r);
        Fusionner(L, p, q, r);
    }
}



int main(int argc, char *argv)
{
    int n = 10;
    int valuesA[] = {1,4,6,8,9,0,2,3,5,7};
    int *valuesB = malloc(n * sizeof(int));

    t_liste listA = {n, valuesA};
    t_liste listB = {n, valuesB};

    TriFusion(listA, 0, 10);

    for(int i=0; i < n;i++)
        printf("%3d", valuesA[i]);
    printf("\n");


    return 0;
}
