#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double Exp(float x, int i)
{
  int j = 0;
  double r = 1;
  while (j < i){
    r *= x;
    j++;
  }
  return r;
}

double SM(float x,int k)
{
  double R = 1;
  int i = 0;
  while (i < k)
  {
    R *= R;
    if(k & 1) R *= x;
    k /= 2;
    i++;
  }
  return R;
}

float Eval_Naif(float *P, uint n, float a)
{
  float R = P[0];
  int i = 1;
  while(i <= n)
  {
    R += (P[i] * Exp(a, i));
    i++;
  }
  return R;
}

float Eval_SM(float *P, uint n, float a)
{
  float R = P[0];
  int i = 1;
  while (i <= n)
  {
    R = R + P[i] * Exp(a,i);
    i++;
  }
  return R;
}

float Eval_Horner(float *P, uint n, float a)
{
  float R = 0;
  int i = 0;

  while(i <= n)
  {
    R = R * a + P[n - i];
    i++;
  }
  return R;
}

float *Creer_Poly(uint n)
{
  float *poly = (float*)malloc((n+1) * sizeof(float));
  srand(time(NULL));
  for(int i = 0; i < n; i++)
    poly[i] = rand() % 9 + 1;

  return poly;
}

int main(int argc, char *argv[])
{
  uint n = atoi(argv[1]);

  float *P = Creer_Poly(n);

  for(int i = 0; i < n; i++)
    printf("%5.2f", P[i]);

  printf("\n");
  printf("%f\n", Eval_Naif(P, n, 17.5));
  printf("%f\n", Eval_SM(P, n, 17.5));
  printf("%f\n", Eval_Horner(P, n, 17.5));


  return 0;
}
