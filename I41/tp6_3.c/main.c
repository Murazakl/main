#include <stdio.h>
#include <stdlib.h>
#define TRUE 1
#define FALSE 0


typedef unsigned long long ullong;
typedef unsigned int uint;


ullong TriBulles(uint *T, uint n)
{
    int i = 0, K = 0, ptr = 0;
    while (ptr < n)
    {
        while (i < n -ptr - 1)
        {
            if(T[i] > T[i+1])
            {
                int tmp = T[i];
                T[i] = T[i+1];
                T[i+1] = tmp;
                K++;
            }
            i++;
        }
        K += i;
        ptr++;
    }
    return K + ptr;;
}




int main()
{
    int T[10] = {84,59,48,19,72,68,10,87,15,47};
    printf("%d", TriBulles(T, 10));

    return 0;
}
