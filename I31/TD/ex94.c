#include <stdio.h>
#include <math.h>



int nbDeChiffres(int x);
int estPair(int x);
int extraitNombre(int x,int n, int lg);
int sommeDesChiffres(int x);

int main()
{
    int n, gauche, droite;
    printf("Donner un nombre: ");
    scanf("%d", &n);
    if (!estPair(n)) printf("le nombre de chiffre n'est pas pair\n");
    else
        gauche = extraitNombre(n, nbDeChiffres(n)/2, nbDeChiffres(n)/2);
        droite = extraitNombre(n, 0, nbDeChiffres(n)/2);
        if (sommeDesChiffres(gauche) == sommeDesChiffres(droite))
        printf("le Nombre %d est couicable\n",n);
        else    printf("le Nombre %d n'est pas couicable\n",n);
}

int nbDeChiffres(int x)
{
    int nb = 0;
    while (x>0) {
        x /= 10;
        nb++ ;
    }
    return nb;
}

int estPair(int x)
{
    return (nbDeChiffres(x) % 2 == 0);
}

int extraitNombre(int x,int n,int lg)
{
    return (int)(x / pow(10, n)) % (int)pow(10, lg);   
}

/*int extraitNombre(int x, int n, int lg)
{
    for (i=0; i<n; i++)
        x /= 10;
    for (j=0; j<lg; j++)
        y *= 10;
    nbr = x % y;
    return nbr;
}*/

int sommeDesChiffres(int x)
{
    int somme = 0, i;
    for (i=1; i<=nbDeChiffres(x); i++)
        somme += (x % (int)(pow(10,i))) / pow(10,i-1);
    return somme;
}