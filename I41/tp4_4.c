#include <stdio.h>
#include <stdlib.h>
#include <time.h>

float *Creer_Poly(uint n);

int main(int argc, char *argv)
{
  int taille;
  printf("Entrer Degrée du polynome: \n");
  scanf("%d", &taille);

  printf("%f\n", *Creer_Poly(taille));
}


float *Creer_Poly(uint n)
{
  int i;
  float *poly = malloc((n+1) * sizeof(float));
  srand(time(NULL));
  for(i = 0; i < n+1; i++)
    poly[i] = rand() % 9 + 1;

  return poly;
}
