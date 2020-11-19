#include <stdio.h>

typedef union
{
	int entier;
	float reel;
} entreel;

int main()
{
	entreel f;
	printf("Entrer un réel: ");
	scanf("%f", &f.reel);
	char signe = (f.entier >> 31) == 0 ? ' ' : '-';
	int exposant = (f.entier << 1) >> 24;
	float mantisse = (f.entier << 9) >> 9;
	/*
		TODO: Calculer la mantisse, le signe et l'exposant.
	*/
	printf("Le réel [%f] est codé comme [%c][%f] fois deux puissance [%d]\n", f.reel, signe, mantisse, exposant);
}