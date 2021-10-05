#include <stdio.h>
#include <stdlib.h>

float Eval_Horner(float *P, float a);

int main(int argc, char *argv[])
{
  float P[] = {1,2,3,4,5};
  printf("%f\n", Eval_Horner(P,2));
}

float Eval_Horner(float *P, float a)
{
  float R = 0;
  int i = 0;

  while(i <= 5)
  {
    R = R * a + P[5 - i];
    i++;
  }
  return R;
}
