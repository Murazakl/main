#include <stdio.h>
#include <stdlib.h>

int estDivisiblePar(int x, int y);

int main()
{
    int x , y;
    printf("Entrer un nombre x: ");
    scanf("%d", &x);
    printf("Entrer un nombre y: ");
    scanf("%d", &y);
    printf("%d est-il divisible par %d (1= oui, 0= non): %d \n", x, y, estDivisiblePar(x, y));
}

int estDivisiblePar(int x, int y)
{
    int tmp;
	if (x % y == 0) tmp = 1;
    else tmp = 0; 
    return tmp;
}