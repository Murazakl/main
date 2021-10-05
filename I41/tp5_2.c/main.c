#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned int uint;

uint *S2L(char *chaine)
{
    int i = strlen(chaine), j = 0;
    int *L = malloc(i * sizeof(int));

    while (j < i)
    {
        L[i-j-1] = chaine[j] - '0';
        j++;
    }
    return L;
}

char *L2S(uint *liste)
{
    int j = 0;
    char *ch = malloc(6 * sizeof(char));

    while (j < 6)
    {
        ch[6-j-1] = liste[j] + '0';
        j++;
    }
    return ch;
}

int main(int argc, char *argv)
{
    uint* inverse = S2L("320154");
    char* inverse2 = L2S(inverse);
    for (int i=0; i < 6; i++)
    {
        printf("%d", inverse[i]);
    }
    printf("\n%s\n", inverse2);
    return 0;
}
