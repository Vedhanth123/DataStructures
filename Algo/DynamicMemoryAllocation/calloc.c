
#include <stdio.h>
#include <stdlib.h>

void main()
{
    int n = 8;
    int *pointer = (int*) calloc(n, sizeof(int)); //  calloc
    int *pointer = (int*) malloc(n * sizeof(int));// malloc
    int *pointer = (int*) realloc(pointer, n* sizeof(int)); // realloc

    if(pointer == NULL)
        printf("Memory not allocated: \n");
    else
    {
        printf("Memory allocated: \n");

        for(int i = 0; i < n; i++)
            pointer[i] = i;
        for(int i = 0; i < n; i++)
            printf("%d\n",*(pointer + i));
    }
    free(pointer);
}
