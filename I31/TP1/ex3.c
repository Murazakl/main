#include <stdio.h>

int main()
{
	char caractere;
	printf("Entrez un caractère: ");
	scanf("%c", &caractere);
	printf("Code ascii de %c: %d\n", caractere, caractere);
	printf("on a fait l'exercice 2\n");
	return 0;
}