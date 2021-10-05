#include <stdio.h>
#include <stdlib.h>

typedef unsigned long long ullong;
typedef unsigned int uint;

ullong TriInsertion(uint *T, uint n)
{
    int i,K = 0, p ,j ,x;
    for(i=1; i < n; i++)
    {
        x = T[i];
        p = i-1;
        while(T[p] > x && p-- > 0)
        {}
        p++;
        for(j=i-1; j>= p; j--)
        {
            T[j+1] = T[j];
            K++;
        }
        T[p] = x;
    }
    return K + i;
}

int main()
{
    int T[10] = {1,2,3,4,5,6,7,8,9,10};
    printf("%3d", TriInsertion(T,10));
    return 0;
}
