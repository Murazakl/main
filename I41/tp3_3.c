#include <stdio.h>
#include <stdlib.h>
#include <string.h>

uint PairOuImpair(uint n);
uint syracuse(uint u0);

int main(){
  uint i = 14;
  uint result = PairOuImpair(10);
  uint result2 = syracuse(i);
  printf("Pair ou Impair: %d\n", result);
  printf("%d\n", result2);
}

uint PairOuImpair(uint n){
  int S;
  if (n%2 == 0){
    S = n/2;
  }
  else S = 3*n+1;
}

uint syracuse(uint u0){
  int u = u0;
  int n = 0;
  while (u > 1){
    u = PairOuImpair(u);
    n++;
  }
  return n;
}
