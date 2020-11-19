#include <stdio.h>
#include <math.h>

int serieGeometrique(int x, int n);

int main()
{
    int x, n;
    printf("Entrer les nombres x et n\n");
    printf("x= ");
    scanf("%d", &x);
    printf("n= ");
    scanf("%d", &n);
    printf("La somme de la série= %d\n",serieGeometrique(x, n));
}

int serieGeometrique(int x, int n)
{
    int somme = 0;
	for (int i = 0; i <= n; i++)
	{
		somme += pow(x, i);
	}
	return somme;
}