#include <stdio.h>

int sommeDesImpairs(int n);

int main()
{
    int n;
    printf("Entrer un nombre n: ");
    scanf("%d", &n);
    printf("La somme des Impaires parmi les n premiers entiers de %d: %d\n",n,sommeDesImpairs(n));
}

int sommeDesImpairs(int n)
{
	int somme = 0;
	for (int i = 0; i < n + 1; i++)
	{
		if (i % 2 == 1)
			somme += i;
	}
	return somme;
}