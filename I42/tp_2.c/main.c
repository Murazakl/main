#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(void)
{

 pid_t pid;
 int n;

 printf("Adresse de n: %p\n", &n);
 n = 0;
 pid = fork();
 if (pid > 0)
     /* incrementation par le processus pere */
     n++;

 if (pid > 0)
        printf("Je suis le pere, n vaut %d\n", n);
 else
        printf("Je suis le fils, n vaut %d\n", n);
 return 0;
}
