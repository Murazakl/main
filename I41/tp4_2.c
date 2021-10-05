#include <stdio.h>
#include <stdlib.h>

int Exp(float x,int k){
  unsigned float r = 1;
  int B[] = {};
  int i = k - 1;

  while(i >= 0)
  {
    R *= R;
    if (B[i] = 1)
      {
        R *= x;
      }
    i--;
  }
  return r;
}

float Eval_SM(float *P, float a){
  float R = P[0];
  int i = 1;
  while (i <= 5){
    R = R + P[i] * Exp(a,i);
    i++;
  }
  return R;
}

int main(int argc;char *argv)
{
  float P = {};
  printf("%f\n", Eval_SM(P,));
}
