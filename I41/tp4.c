#include <stdio.h>
#include <stdlib.h>

typedef unsigned long long ullong;
typedef unsigned int uint;

typedef struct
{
  ullong matrice[2][2];
}tmat;

tmat produit(tmat A, tmat B)
{
  int i = 0, j;
  tmat res;
  while(i < 2)
  {
    j = 0;
    while(j < 2)
    {
      res.matrice[i][j] = 0;
      for (int k = 0; k < 2; k++)
        res.matrice[i][j] += (A.matrice[i][k] * B.matrice[k][j]);
      j++;
    }
    i++;
  }
  return res;
}

tmat puissance(tmat M, uint n)
{
  tmat res = M;
  for(int i = 1; i < n; i++)
    res = produit(res, M);
  return res;
}

tmat SM(tmat M, uint n)
{
  tmat id;
  id.matrice[0][0] = 1;
  id.matrice[0][1] = 0;
  id.matrice[1][0] = 0;
  id.matrice[1][1] = 1;
  while (n != 0)
  {
    if(n & 1) id = produit(id, M);
    M = produit(M, M);
    n /= 2;
  }
  return id;
}

ullong Fib(uint n)
{
  tmat A;
  A.matrice[0][0] = 1;
  A.matrice[0][1] = 1;
  A.matrice[1][0] = 1;
  A.matrice[1][1] = 0;
  ullong tmp, tmp2;
  for(int i = 2; i <= n; i++)
  {
    tmp = A.matrice[0][0];
    A.matrice[0][0] = A.matrice[0][0] + A.matrice[0][1];
    tmp2 = A.matrice[0][1];
    A.matrice[0][1] = tmp;
    A.matrice[1][0] = tmp;
    A.matrice[1][1] = tmp2;
  }
  return A.matrice[0][1];
}

ullong FibSM(uint n)
{
  tmat A;
  A.matrice[0][0] = 1;
  A.matrice[0][1] = 1;
  A.matrice[1][0] = 1;
  A.matrice[1][1] = 0;
  A = SM(A, n);
  return A.matrice[0][1];
}

int main(int argc, char *argv[])
{
  /*tmat A, B;
  ullong n;
  for(int i = 0; i < 2; i++)
    for(int j = 0; j < 2; j++)
    {
      printf("Valeur pour A[%d][%d]: ", i, j);
      scanf("%llu", &n);
      A.matrice[i][j] = n;
    }
  for(int k = 0; k < 2; k++)
    for(int l = 0; l < 2; l++)
    {
      printf("Valeur pour B[%d][%d]: ", k, l);
      scanf("%llu", &n);
      B.matrice[k][l] = n;
    }

  tmat res = produit(A, B);

  printf("%llu, %llu \n%llu, %llu\n", res.matrice[0][0], res.matrice[0][1], res.matrice[1][0], res.matrice[1][1]);

  printf("\n");

  tmat res2 = puissance(A, 3);

  printf("%llu, %llu \n%llu, %llu\n", res2.matrice[0][0], res2.matrice[0][1], res2.matrice[1][0], res2.matrice[1][1]);

  tmat res3 = SM(A, 3);

  printf("%llu, %llu \n%llu, %llu\n", res3.matrice[0][0], res3.matrice[0][1], res3.matrice[1][0], res3.matrice[1][1]);
*/
  ullong m;
  printf("Nombre Fibo: ");
  scanf("%llu", &m);

  printf("%llu\n", Fib(m));
  printf("%llu\n", FibSM(m));

  return 0;
}
