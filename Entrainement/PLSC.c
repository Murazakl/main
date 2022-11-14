#include <stdio.h>
#include <stdlib.h>

//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
//  DEFINITIONS
//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

// En cas d'erreur sur les arguments
#define ERREUR_NBARGS 1

// Macro max
#define max(a,b) ( ((a) > (b)) ? (a) : (b) )

// Entiers non signés
typedef unsigned char uchar;
typedef unsigned int uint;

// Structure de chaîne de caractères
typedef char *tmot;

///////////////////////////////////////////////////////////////
// À COMPLÉTER - À COMPLÉTER - À COMPLÉTER - À COMPLÉTER 
// Renvoie la longueur du <mot> (chaine qui finit par '\0')
///////////////////////////////////////////////////////////////
uint len(tmot mot){



}

///////////////////////////////////////////////////////////////
// À COMPLÉTER - À COMPLÉTER - À COMPLÉTER - À COMPLÉTER 
// Renvoie VRAI (1) si u est un préfixe de v et FAUX (0) sinon.
///////////////////////////////////////////////////////////////
uchar EstPrefixe(tmot u, tmot v){



}

///////////////////////////////////////////////////////////////
// À COMPLÉTER - À COMPLÉTER - À COMPLÉTER - À COMPLÉTER 
// Renvoie VRAI (1) si u est une ss-séq. de v et FAUX (0) sinon.
///////////////////////////////////////////////////////////////
uchar EstSousSeq(tmot u, tmot v){



}


///////////////////////////////////////////////////////////////
// Affiche la table L des Longueurs de PLSC
///////////////////////////////////////////////////////////////
void AfficherTable(uint **L, tmot u, tmot v){
  uint i,j;
  uint n = len(u);
  uint m = len(v);

  printf("     ");
  for (i = 0; i < m + 1; i++)
    printf("%3c",v[i]);
  printf("\n");  
  for (i = 0; i < n + 1; i++)
    {
      if (i > 0) 
	printf("%2c",u[i - 1]);
      else printf("  ");
      for (j = 0; j < m + 1; j++)
	{
	  if ((i > 0) && (j >0) && (u[i - 1] == v[j - 1]))
	    printf("%3u",L[i][j]);	  
	  else
	    printf("%3u",L[i][j]);	  
	}
      printf("\n");
    }   
}


///////////////////////////////////////////////////////////////
// À COMPLÉTER - À COMPLÉTER - À COMPLÉTER - À COMPLÉTER 
// Construit et renvoie la table L des longueurs des PLSC
// de deux mots u et v.
///////////////////////////////////////////////////////////////
uint **LPLSC(tmot u, tmot v){



}

///////////////////////////////////////////////////////////////
// À COMPLÉTER - À COMPLÉTER - À COMPLÉTER - À COMPLÉTER 
// Renvoie une PLSC des mots u et v.
///////////////////////////////////////////////////////////////
tmot PLSC(tmot u, tmot v){



}


int main(int argc, tmot argv[])
{
  if (argc < 2)
    {
      printf("Syntaxe: %s mot1 mot2\n",argv[0]);
      return ERREUR_NBARGS;
    }

  tmot u = argv[1];
  tmot v = argv[2];
  
  uint **L = LPLSC(u,v);  
  AfficherTable(L,u,v);

  printf("%s",PLSC(u,v))
  return 0;
}
