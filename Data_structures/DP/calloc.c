#include <stdio.h>
#include <stdlib.h>

void main()
{

    // allocating memory using calloc
    
    int n = 8;
    
    pointer = (int*) calloc(n, sizeof(int));

    if(pointer == NULL)
        printf("Memory not allocated: \n");
    
    else
    {
        printf("Memory allocated: \n");

        // inserting values into memory
        for(int i = 0; i < n; i++)
            pointer[i] = i;

        // accessing values from memory
        for(int i = 0; i < n; i++)
            printf("%d\n",*(pointer + i));

    }
}
