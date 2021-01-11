#include <stdio.h>
#include <stdlib.h>

// 19124-CM-111 Vedhanth
void main()
{
    int *pointer;

    // asking user for amount of memory to be allocated
    int n;
    printf("Enter the size of memory to be allocated: \n");
    scanf("%d", &n);

    // allocating memory using malloc
    pointer = (int*) malloc(sizeof(int) * n);

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


    // deallocating memory
    free(pointer);

    printf("Trying to access memory after freeing memory: \n");
    for(int i = 0; i < n; i++)
    {
        printf("%d\n",pointer[i]);
    }
}
