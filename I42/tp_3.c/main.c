#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <sys/types.h>

pid_t pid,ppid;

void traitersignal(int sig)
  {
     printf("PID de mon fils: %d\n", pid);
  }

int main(void)

{
  ppid = getpid();
  pid = fork();
  if (pid == 0)
    {
      sleep(5);
      kill(ppid, SIGUSR1);
    }
  else
    {
      signal(SIGUSR1, traitersignal);
      pause();
    }
  exit(0);
}
