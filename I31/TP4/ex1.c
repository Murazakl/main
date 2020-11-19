#include <stdio.h>
#include <stdlib.h>

/*int main(int argc, char *argv[])
{
    FILE* fichier = NULL;
 
    fichier = fopen("test.txt", "w");
 
    if (fichier != NULL)
    {
        fputc('A', fichier); // Écriture du caractère A
        fclose(fichier);
    }
 
    return 0;
}*/

/*int main(int argc, char *argv[])
{
    FILE* fichier = NULL;
 
    fichier = fopen("test.txt", "w");
 
    if (fichier != NULL)
    {
        fputs("Cette prof c'est de la merde", fichier);
        fclose(fichier);
    }
 
    return 0;
}*/                               

/*int main(int argc, char *argv[])
{
    FILE* fichier = NULL;
    int age = 0;
 
    fichier = fopen("test.txt", "w");
 
    if (fichier != NULL)
    {
        // On demande l'âge
        printf("Quel age avez-vous ? ");
        scanf("%d", &age);
 
        // On l'écrit dans le fichier
        fprintf(fichier, "Le Monsieur qui utilise le programme, il a %d ans", age);
        fclose(fichier);
    }
 
    return 0;
}*/

/*#define TAILLE_MAX 1000
 
int main(int argc, char *argv[])
{
    FILE* fichier = NULL;
    char chaine[TAILLE_MAX] = "";
 
    fichier = fopen("test.txt", "r");
 
    if (fichier != NULL)
    {
        while (fgets(chaine, TAILLE_MAX, fichier) != NULL) // On lit le fichier tant qu'on ne reçoit pas d'erreur (NULL)
        {
            printf("%s", chaine); // On affiche la chaîne qu'on vient de lire
        }
 
        fclose(fichier);
    }
 
    return 0;
}*/

void ecrire_livre(char cote, char titre, int annee)
{
    FILE* fichier = NULL;

    fichier = fopen("test.txt", "w");

    if (fichier != NULL)
    {
        printf("Titre du Livre: ");
        scanf("%s", &titre);
        printf("Côte du Livre: ");
        scanf("%s", &cote);
        printf("Annee du Livre: ");
        scanf("%d", &annee);

        fprintf("Titre: %s\n Côte: %s\n Annee: %d\n", titre, cote, annee);
        fclose(fichier);
    }
    return 0;
}

int main()
{
    void ecrire_livre(char cote, char titre, int annee);
}