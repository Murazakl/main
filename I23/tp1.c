#include <stdio.h>
/*#define PRINT(int) printf("%d\n", int)*/
#define PRINTX printf("%d\n",x)
#define PRINT(int) printf("int = %d\n",int)
#define PRINT3(x,y,z)\
printf("x=%d\ty=%d\tz=%d\n",x,y,z)
#define TYPE int


int main() {

/*EXERCICE 1*/

  /*printf("Hello World \n");*/

/*EXERCICE 2*/
/*EXO 12*/

  /*int x, y, z;
  x = 2; y = 1; z = 0;
  x = x && y || z; PRINT(x);
  PRINT(x || !y&&z);

  x = y = 1;
  z = x ++ -1; PRINT(x); PRINT(z);
  z += -x ++ + ++ y; PRINT(x); PRINT(z);
  z = x / ++ x; PRINT(z);*/

/*EXO 14*/

  /*int x;

  x = -3+4*5-6; printf("%d\n",x);
  x = 3+4%5-6; printf("%d\n",x);
  x = -3*4%-6/5; printf("%d\n",x);
  x = (7+6)%5/2; printf("%d\n",x);*/

/*EXO 16*/

  /*int x = 2, y, z;

  x *= 3+2; PRINTX;
  x *= y = z = 4; PRINTX;
  x = y == z; PRINTX;
  x == (y=z); PRINTX;*/

/*EXO 17*/

  /*int x = 1, y = 1, z = 1;

  x += y += z;
  PRINT(x < y ? y : x);

  PRINT(x < y ? x ++ : y ++);
  PRINT(x); PRINT(y);

  PRINT(z += x < y ? x ++ : y ++);
  PRINT(y); PRINT(z);

  x = 3; y = z = 4;
  PRINT((z >= y >= x) ? 1 : 0);
  PRINT(z >= y && y >= x);*/

/*EXO 19*/

  /*int x, y, z;

  x = 03; y = 02; z = 01;
  PRINT(x | y & z);
  PRINT(x | y & ~z);
  PRINT(x ^ y & ~z);
  PRINT(x & y && z);

  x = 1; y = -1;
  PRINT( !x | x);
  PRINT(~x | x);
  PRINT(x^x);
  x <<= 3; PRINT(x);
  y <<= 3; PRINT(y);
  y >>= 3; PRINT(y);*/

/*EXO 20*/

  /*int x, y, z;
  x = y = z = 1;
  ++x || ++y && ++z; PRINT3(x,y,z);
  x = y = z = 1;
  ++x && ++y || ++z; PRINT3(x,y,z);
  x = y = z = 1;
  ++x && ++y && ++z; PRINT3(x,y,z);
  x = y = z = -1;
  ++x && ++y || ++z; PRINT3(x,y,z);
  x = y = z = -1;
  ++x || ++y && ++z; PRINT3(x,y,z);
  x = y = z = -1;
  ++x && ++y && ++z; PRINT3(x,y,z);*/

/*EXO 25 à recopier si l'envie*/
/*EXO 26 à recopier si l'envie*/

/*EXERCICE 3*/

  /*char ch;
  printf("Entrez un caractère:\n");
  scanf("%c", &ch);
  printf("ASCII de %c: %d\n", ch, ch);
  printf("on a fait l'exercice 2\n");*/

/*EXERCICE 4*/

  /*int x, y ,m;
  printf("Entrez deux entiers x et y:\n");
  scanf("%d", &x);
  scanf("%d", &y);
  m = x - y;
  if (m < 0) m = y;
  else m = x;
  printf("%d\n", m);*/

/*EXERCICE 5*/

  /*int date, a, m, j;
  printf("Entrez une date codée:\n");
  scanf("%d", &date);
  a = date / 10000;  printf("Année:%d\n", a);
  date -= (a * 10000);
  m = date / 100;  printf("Mois:%d\n", m);
  date -= (m * 100);
  j = date;  printf("Jour:%d\n", j);*/

}

/*EXERCICE 6*/

  void fonction(TYPE n)
  {
    TYPE i;
    int j, taille;
    taille = 8 * sizeof(TYPE);
    for (j = 0; j < taille; j++)
    {
      i = 1 << (taille - j -1);
      if (n & i) printf("1");
      else printf("0");
    }
    printf("\n");
  }
