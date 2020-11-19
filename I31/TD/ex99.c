#include <stdio.h>

int main()
{
const int N = 5;
int nombres[N];

for (int i = 0; i < N; i++)
{
printf("Entrer un nombre: ");
scanf("%d", &nombres[i]);
}

for (int i = N-1; i >=0; i--)
printf("%d\n", nombres[i]);
}