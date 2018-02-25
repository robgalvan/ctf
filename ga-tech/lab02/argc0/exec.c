#include <unistd.h>
#include <stdio.h>  
#include <stdlib.h>  
#include <errno.h> 
  
char* readFileBytes(const char *name)  
{  
    FILE *fl = fopen(name, "r");
    fseek(fl, 0, SEEK_END);  
    long len = ftell(fl);  
    char *ret = malloc(len);  
    fseek(fl, 0, SEEK_SET);  
    fread(ret, 1, len, fl);  
    fclose(fl);  
    return ret;  
}

  
int main()
{
	char *envp = readFileBytes("/home/vagrant/cs6265/lab02/argc0/payload");
	char *env[] = {envp, NULL};
	char *args[] = {NULL};
	execve("/home/vagrant/cs6265/lab02/argc0/target", args, env);
         
	/* only get here on an exec error */
        if (errno == ENOENT)
        	printf("child.exe not found in current directory\n");
        else if (errno == ENOMEM)
        	printf("not enough memory to execute child.exe\n");
        else
        	printf("error #%d trying to exec child.exe\n", errno);
}
