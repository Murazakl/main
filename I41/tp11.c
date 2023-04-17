#include <stdio.h>
#include <stdlib.h>

typedef unsigned int uint;

typedef struct
{
  float nombre;
  char op;
  enum {unaire, binaire, nombre} type;
} TJETON, *TEXPR;

typedef struct tcell
{
  float val;
  struct tcell *suivant;
} TCELL, *TLISTE;

typedef TLISTE TPILE;

TJETON Chaine2Jeton(char *chaine)
{
  TJETON jeton;
  float nombre;

  if (sscanf(chaine, "%f", &nombre) == 1)
  {
    jeton.nombre = nombre;
    jeton.type = nombre;
    return jeton;
  }
  switch (*chaine)
  {
    case '+':
      jeton.op = '+';
      jeton.type = binaire;
      break;
    case '-':
      jeton.op = '-';
      jeton.type = binaire;
      break;
    case '*': case 'x':
      jeton.op = '*';
      jeton.type = binaire;
      break;
    case '/':
      jeton.op = '/';
      jeton.type = binaire;
      break;
    case '_':
      jeton.op = '_';
      jeton.type = unaire;
      break;
    default :
      break;
  }
  return jeton;
}

 TEXPR Arg2Expr(int argc, char *argv[])
 {
   TEXPR res = calloc(argc, sizeof(TJETON));
   for(int i = 0; i < argc-1; i++)
    res[i] = Chaine2Jeton(argv[i+1]);

  return res;
 }

/*TPILE Empiler(TPILE pile, float nombre)
{
  TPILE aux;
  aux = malloc(sizeof(TCELL));
  aux -> val = nombre;
  aux -> suivant = pile;

  return aux;
}*/

void Empiler(TPILE *pile, float nombre)
{
  TPILE aux = malloc(sizeof(TCELL));
  aux -> val = nombre;
  aux -> suivant = *pile;
  *pile = aux;
}

/*TPILE Depiler(TPILE pile, float *nombre)
{
  TPILE aux = pile -> suivant;
  *nombre = pile -> val;
  free(pile);

  return aux;
}*/

float Depiler(TPILE *pile)
{
  float res = (*pile) -> val;
  TPILE aux = (*pile) -> suivant;
  free(*pile);
  *pile = aux;

  return res;
}

void AfficherPile(TPILE pile)
{
  TLISTE e = pile;
	if(e != NULL)
  {
		printf("%f ",e -> val);
		e = e -> suivant;
		while(e != NULL)
    {
			printf("%f ",e -> val);
			e = e -> suivant;
		}
	}
  free(e);
	printf("\n");
}

float operer(float x,float y, char op)
{
  float res;
  switch (op)
  {
    case '+':
      res = x + y;
      break;
    case '-':
      res = x - y;
      break;
    case 'x': case '*':
      res = x * y;
      break;
    case '/':
      res = x / y;
      break;
    case '_':
      res = -x;
      break;
    default:
      break;
  }
  return res;
}

float Evaluer(TEXPR expr, uint n)
{
  int i = 0;
  TLISTE pile = NULL;
  while (i < n)
  {
    if (expr[i].type == binaire)
    {
      float y = Depiler(&pile);
      float x = Depiler(&pile);
      float z = operer(x, y, expr[i].op);
      Empiler(&pile, z);
    }
    else if (expr[i].type == unaire)
    {
      float x = Depiler(&pile);
      float y = 0.0;
      float z = operer(x, y, expr[i].op);
      Empiler(&pile, z);
    }
    else
      Empiler(&pile, expr[i].nombre);
    i++;
  }
  return Depiler(&pile);
}

int main(int argc, char *argv[])
{
  uint n = argc-1;
  TEXPR expr;

  if (n < 1)
  {
    printf("Syntaxe: %s expr\n", argv[0]);
    return 1;
  }
  else
    expr = Arg2Expr(argc, argv);

  float res = Evaluer(expr, n);

  printf("%f\n", res);

  free(expr);

  return 0;
}
