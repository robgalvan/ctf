#include <stdio.h>
#include <stdlib.h>

int main(int argc,char * argv[])
{
	int time_check = atoi(argv[1]);
	int store = time(0);
	while(store < time_check)
	{
		printf("Waiting\n");
		store = time(0);
	}
	return 0;
}
