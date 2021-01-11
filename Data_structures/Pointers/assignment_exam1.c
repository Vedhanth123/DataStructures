# include <stdio.h>
# include <stdlib.h>

// program to create dynamic memory using malloc

void main()
{  
    // declaring a pointer
    int *ptr; 

    // asking user for amount of memory to be allocated
    int n;
    printf("Enter the amount of memory to be allocated :\n");
    scanf("%d",&n);

    // declaring an iterator
    int i;

    // allocating memory using malloc and assigning its address to a pointer
    ptr = (int*) malloc(n * sizeof(int));

    if(ptr == NULL)
    {
        printf("memory allocation unsuccessful :\n");
    }
    else
    {
        printf("memory allocated sucessfully :\n");
        // assigning values to the memory

        for (i = 0; i < n; i ++);
        {
            *(ptr+i) = n;
        }

        // accessing values stored in the memory
        for (i = 0; i < n; i++)
        {
            printf("%d\n",*(ptr+i));
        }
    }

}