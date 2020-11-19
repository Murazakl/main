#include <stdio.h>

int estDansRectangle(int x1, int y1, int x2, int y2, int x, int y);
int estSurContour(int x1, int y1, int x2, int y2, int x, int y);
int estExterieur(int x1, int y1, int x2, int y2, int x, int y);
int estInterieur(int x1, int y1, int x2, int y2, int x, int y);

int main()
{
    int x1, x2, y1, y2, x, y;
    printf("Entrer des nombres x1, y1, x2, y2\n");
    printf("x1= ");
    scanf("%d", &x1);
    printf("y1= ");
    scanf("%d", &y1);
    printf("x2= ");
    scanf("%d", &x2);
    printf("y2= ");
    scanf("%d", &y2);
    printf("Entrer Coordonnée du points (x,y): ");
    printf("x= ");
    scanf("%d", &x);
    printf("y= ");
    scanf("%d", &y);
    printf("Le point est dans le rectangle ? %d\n",estDansRectangle(x1, x2, y1, y2, x, y));
    printf("Le point est sur le contour ? %d\n",estSurContour(x1, x2, y1, y2, x, y));
    printf("Le point est à l'extérieur ? %d\n",estExterieur(x1, x2, y1, y2, x, y));
    printf("Le point est à l'intérieur ? %d\n",estInterieur(x1, x2, y1, y2, x, y));

}

int estDansRectangle(int x1, int y1, int x2, int y2, int x, int y)
{
	return x > x1 && y < y1 && x < x2 && x > y2;
}

int estSurContour(int x1, int y1, int x2, int y2, int x, int y)
{
	return (x >= x1 && x <= x2 && y == y2) ||
				 (x >= x1 && x <= x2 && y == y1) || (x == x1 && y >= y2 && y <= y1) || (x == x2 && y >= y2 && y <= y1);
}

int estExterieur(int x1, int y1, int x2, int y2, int x, int y)
{
	return !estDansRectangle(x1, y1, x2, y2, x, y) && !estSurContour(x1, y1, x2, y2, x, y);
}

int estInterieur(int x1, int y1, int x2, int y2, int x, int y)
{
	return estDansRectangle(x1, y1, x2, y2, x, y) && estSurContour(x1, y1, x2, y2, x, y);
}