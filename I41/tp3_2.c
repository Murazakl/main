#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void Affiche_Liste(int *liste, ushort n);
void TriSelection(int *liste, ushort n);

int main(){
  int n, i;
  printf("Nombres d'entiers que vous voulez triez: ");
  scanf("%d",&n);

  int *liste = (int*)malloc(sizeof(int) * n);
  printf("\n");

  for (i=0; i < n; i++){
    printf("Donner l'entier %d: ", i);
    scanf("%d", &liste[i]);
  }

  Affiche_Liste(liste,n);
  TriSelection(liste,n);
  Affiche_Liste(liste,n);

  return 0;
}

void Affiche_Liste(int *liste, ushort n)
{
  for(int i = 0; i < n-1; i++)
    printf("%3d", liste[i]);
  printf("\n\n");
}

void TriSelection(int *liste, ushort n){
  int i, j, tmp, min;
  for (i=0; i < n-1; i++){
    min = i;
    for (j=i+1; j < n; j++)
      if (liste[j] < liste[min])
        min = j;
    if (min != i){
        tmp = liste[i];
        liste[i] = liste[min];
        liste[min] = tmp;
    }
  }
}
