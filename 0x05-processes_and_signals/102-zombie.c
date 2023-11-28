#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"
/**
 * main - create five zombie processess
 *
 * Return: nothing
 */
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

void main(void)
{
	pid_t child;
	int i;

	for(i = 0; i<5; i++)
	{
		child = fork();
		if (child == 0)
		{
			printf("Zombie process created, PID: %d\n",getpid());
			exit(0);
		}
	}
	infinite_while();
}
