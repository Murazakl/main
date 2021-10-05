#include <stdio.h>
#include <stdlib.h>

int Exp(float x, int i);
float Eval_Naif(float *P, float a);

int main(int argc, char *argv)
{
  float P[] = {1,2,3,4,6};
  printf("%f\n", Eval_Naif(P, 17.5));
}

int Exp(float x, int i)
{
  int j = 0;
  float r = 1;
  while (j < i){
    r *= x;
    j++;
  }
  return r;
}

float Eval_Naif(float *P, float a)
{
  float R = P[0];
  int i = 1;
  while (i <= 5){
    R = R + P[i] * Exp(a,i);
    i++;
  }
  return R;
}
