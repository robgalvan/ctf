#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main(){

	char *a = malloc(255);
	char *b = malloc(255);
	strcpy(a,"hello");
	
	printf("%p : %s \n",a, a);
	printf("%p\n",b);


	free(a);
	char *c = malloc(255);

	printf("%p : %s\n",c,c);




}