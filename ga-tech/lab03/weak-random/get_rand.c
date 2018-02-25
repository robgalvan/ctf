#include <stdio.h>
#include <stdlib.h>
#define MAX 50
int main(int argc, char * argv[])
{
	int offset = atoi(argv[1]);
	unsigned int store = time(0)+offset; 
	int i = 0;
	for(;i<MAX;i++)
	{
		srand(store);
		printf("time = %d value = %d\n",store,rand());
		store++;
	}
	return 0;

}
