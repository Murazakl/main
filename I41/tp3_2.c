#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void TriSelection(int *liste, ushort n);

int main(){
  int n;
  int i;
  printf("Nombres d'entiers que vous voulez triez: ");
  scanf("%d",&n);
  int liste[n];
  printf("\n");
  for (i=0; i < n; i++){
    printf("Donner l'entier %d: ", i+1);
    scanf("%d", &liste[i]);
  }
  TriSelection(liste,n);
  for(i=0; i < n; i++)
    printf("%3d", liste[i]);
  printf("\n\n");
  return 0;
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
