#include <stdio.h>
#include <conio.h>


// program to implement bubble sort
void main()


// bubble sort is swapping elements untill and unless it gets sorted
{
    // initializing array
    int array[5] = {99,88,77,66,55};

    // looping the swapping phases
    for (int i = 0; i < 5; i++)
    {
        // swapping the elements in a loop
        for(int j = 0; j < 4; j++)
        {
            // checking if the neighbour elements are greater than the previous one
            if(array[j] > array[j+1])
            {
                // swapping the elements
                int swap = array[j];
                array[j] = array[j+1];
                array[j+1] = swap;   
            }
        }
    }

    // printing the sorted elements in the array
    printf("Swapped array: \n");
    for (int i = 0; i < 5; i ++)
    {
        printf("%d\n",array[i]);
    }
    
    getch();
    
}
