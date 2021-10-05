#include <stdio.h>

int main()
{
  tbool: typedef enum {FALSE = 0, TRUE = 1} tbool;
  tbool t = CommencePar("Bonjour","Bon");
  printf("%d\n", t1);
}

tbool CommencePar(char * mot, char * deb)
{
  uint T_deb = strlen(deb);
  if (T_deb > strlen(mot))
    return FALSE;

  for (int i=0; i < strlen(mot); i++)
    if (mot[i] != deb[i]) return FALSE;
  return TRUE;
}
