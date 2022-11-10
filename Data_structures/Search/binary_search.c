#include <stdio.h>
#include <conio.h>


// 1,2,3,4,5

// algorithm on binary search

// 1) search for the number 4

// 2) pickup the center element of the array as key

// 3) if the center part of the array is less than 4
// then don't look into left part of array anymore

// 4) if the center part of the array is greater than 4
// then don't look into right part of the array anymore

// 5) continue this process till the element is found

int array[5] = {1,2,3,4,5};

int binary_search(int *array, int key, int front, int last)
{
    int mid;

    while(!(front > last))
    {
        // finding the key element which is at the center of the array
        mid = (front + last)/2;

        // checking if element is found
        if(array[mid] == key)
        {
            return mid;
        }

        if(array[mid] < key)
        {
            front = mid + 1;
        }
        else
        {
            last = mid - 1;
        }
    }

}

void main()
{

    int i;
    
    // asking user element to be searched

    printf("%d",binary_search(array, key, 0, 5-1));
    
    getch();

}
