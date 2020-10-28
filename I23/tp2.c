#include <stdio.h>
#include <stdlib.h>

int pgcd(int p, int q);

int main(){

  /*EXERCICE 1*/

  /*int a, b, x=1;
  char op;
  do {
    printf("Entrer une opération (format a op b):");
    scanf("%d %c %d", &a, &op, &b);
    switch (op){
      case '+':
        printf("%d\n", a + b);
        break;
      case '-':
        printf("%d\n", a - b);
        break;
      case '*':
        printf("%d\n", a * b);
        break;
      case '/':
        printf("%d\n", a / b);
        break;
      case '%':
        printf("%d\n", a % b);}
    printf("Continue?(1=oui 0=non): ");
    scanf("%d", &x);
} while (x==1);*/


/*EXERCICE 2*/

  /*int n, i = 0;
  printf("entrer un nombre entier pour n: ");
  scanf("%d", &n);
  while (i * i < n) { i++;
  }
  printf("Le plus petit carre supérieur a %d est %d\n",n,i*i);*/


/*EXERCICE 3*/

  /*int n;
  printf("entrer un nombre entier pour n:");
  scanf("%d", &n);
  int q = n, i = 0;
  do {
    q /= 10;
    i++;
  }
  while (q > 0);
  printf("Le nombre de chiffre du nombre %d est de %d\n",n,i);


/*EXERCICE 4*/

  /*int n, i=1, somme=0;
  printf("entrer un nombre pour n: ");
  scanf("%d", &n);
  if (n > 0)  {for (i; i<=n; i++)
      somme += (i*i);
    printf("La somme est %d\n",somme);}
  else printf("Erreur: n doit être positif et supérieur à 0\n");*/


/*EXERCICE 5*/

  /*int n, compt=0;
  float moy, somme=0.0;
  do{
    printf("Entrer une valeur de n: ");
    somme += n;
    scanf("%d", &n);
    compt++;
  }
  while (n != 0);
  moy = somme / compt;
  printf("La moyenne vaut %f\n",moy);*/


/*EXERCICE 6*/

  /*int p, q;
  printf("Entrer les nombres p et q:\n");
  printf("p =");
  scanf("%d", &p);
  printf("q =");
  scanf("%d", &q);

  printf("pgcd(%d, %d) = %d\n",p,q,pgdc(p, q));*/

}

/*EXERCICE 11*/


int est_premier(int n)
{
  for(int i = 2; i<n; i++)
    if (n % i == 0) return 0;
  return 1;
}

void premiers_premier(int n)
{
  if (!est_premier(n))
    exit(EXIT_FAILURE);

  for (int i = 0; i<n; i++)
    if (est_premier(i))
      printf("%d est aussi un nombre premier\n",i);
}
