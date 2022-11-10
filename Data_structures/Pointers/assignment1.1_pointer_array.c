#include <stdio.h>

// accessing array elements using pointer

void main()
{
    // initializing array with elements in it
    int array[5] = {2000,3000,4000,5000,6000};

    // initializing pointer
    int *pointer = array;

    // accessing elements of array using pointer
    for(int i = 0; i < 5; i++)
    {
        printf("%d",pointer[i]);
    }
    
    // 19124-CM-111 Vedhanth
}