#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main()
{
	int fd = 2;
	while(fd != 3)
	{	
		fd = open("/proc/flag", O_RDONLY);
	}
	pid_t id = fork();
	char *arg[] = {"/home/vagrant/cs6265/lab04/fd-const/target",NULL};
	char *env[] = {NULL};

	if(id == 0)
	{
		execve("/home/vagrant/cs6265/lab04/fd-const/target",arg,env);
	}
	else
	{
		printf("Could not execute\n");
	}
}
