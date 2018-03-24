#include <stdio.h>
#include <stdlib.h>


int main(){

    int *a = malloc(8);
    int *b = malloc(8);
    int *c = malloc(8);

    printf("a: %p , b: %p, c: %p\n",a,b,c);

    free(a);
    //fastbin HEAD->a->TAIL

    free(b);
    //fastbin HEAD->b->a->TAIL

    free(a);
    //fastbin HEAD->a->b->a->TAIL

    
    int *d = malloc(8); //will be set to a
    int *e = malloc(8); //will be set to b
    int *f = malloc(8); //should be set to a also

    printf("d: %p , e: %p, f: %p\n",d,e,f);











}
