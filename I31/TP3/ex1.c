#include <stdio.h>

int absolue(int x);

int main()
{
    int x;
    printf("Entrer un entier: ");
    scanf("%d", &x);
    printf("%d\n", absolue (x));
}

int absolue(int x)
{
    return x < 0 ? -x : x;
}