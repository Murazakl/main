#include <stdio.h>
#include <stdlib.h>

typedef unsigned long long int ullong;
typedef unsigned char uchar;

ullong Factorielle(uchar n)
{
    ullong result = 1;
    while (n > 1)
    {
        result *= n;
        n--;
    }
    return result;
}

int main(int argc, char **argv)
{
    printf("%ld", Factorielle(20));
    return 0;
}
