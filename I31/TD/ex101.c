#include <stdio.h>

int main()
{
    int N = 10, x = 6;
	int A[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

	int isFind = 0;
	for (int i = 0; i < N; i++)
		if (isFind || A[i] == x)
		{
			isFind = 1;
			A[i] = A[i + 1];
		}
	if (isFind)
		N--;

	for (int i = 0; i < N; i++)
		printf("%d ", A[i]);
        printf("\n");
}


/*   Version 2   
#define N 10

int main()
{
    int x, A[N]={2,4,1,9,8,5,6,7,1,6},i=0,tmp = 0;
    printf("Entrer une valeur de x: ");
    scanf("%d",&x);
    while ((x != A[i])&&(i<N)) 
    {
        i++;
    }
    if (i == N) printf("Pas de x dans le tableau");
    else
    {
        for (i;i<N-1;i++)
        {
            tmp = A[i];
            A[i] = A[i+1];
            A[i+1] = tmp;
        };
        for (i=0;i<N-2;i++) 
        {
            printf("%d\n",A[i]);
        }
    }

}


/*    2)    
#define N 10
int main(){
        int A[N]={2,4,1,9,9,5,6,7,1,6};
        int i, x, j;
int c=0;
        printf("Entrer x: ");
        scanf("%d", &x);
        for(i=0;i<N;i++)
        {
                if(A[i]==x)
                {
                        c++;
                        for(j=i;j<N-1;j++)
                                A[j]=A[j+1];
                  i--;
                 
                }
        
        }
        for (i = 0; i < N-c; i++)
        printf("%d ", A[i]);
        printf("\n");
}*/