#include <stdio.h>
#include <stdlib.h>

void main()

{
    
    int n = 10;
    
    // allocating memory using calloc
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
    
    printf("Enter the memory to be reallocated: \n");
    scanf("%d",&n);

    // reallocating memory
    pointer = (int*) realloc(pointer, n*sizeof(int));

    // checking if memory reallocated
    if(pointer == NULL)
        printf("Memory not reallocated: \n");
    
    else
    {
        printf("Memory reallocated:\n");

        for(int i = 0; i < n; i++)
            pointer[i] = i;

        // accessing values from memory
        for(int i = 0; i < n; i++)
            printf("%d\n",*(pointer + i));

    }

    
}
