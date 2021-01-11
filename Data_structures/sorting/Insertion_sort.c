#include <stdio.h>

int swap(int *a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void main()
{
    // create an array
    int array[6] = {9,8,10,6,5,212};

    // one part of the array is sorted and another part of the array is unsorted

    // start from the index 1 and check the elements before it.

    for(int i = 1; i < 6; i++)
    {
        // selecting element
        int selected_element = array[i];

        // iterating through array from right to left to check
        // if the element is less than the previous elements
        int j = i - 1;

        // if the selected element is smaller than the previous elements then swap the elements
        while(j >= 0 && selected_element < array[j])
        {
            swap(&array[j],&array[j+1]);
            j -= 1;
        }
        // swap(&selected_element, &array[j+1]);

    }

    for(int i = 0; i < sizeof(array)/sizeof(int); i++)
    {
        printf("%d\n",array[i]);
    }
    
}