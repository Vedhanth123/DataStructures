#include <stdio.h>

// To find the min element of the array

// 1) Check the value of each and every element of the array
// 3) if there is another minimum element of the array then replace it. else leave it
// 4) continue the process till you reach the last index of the array

int min_element_of_array_using_rec(int *array);
int recursion(int *array, int min, int index);

int recursion(int *array, int min, int index)
{
    // 4) continue the process till you reach the last index of the array
    if(index == 5)
    {
        return min;
    }
    else
    {
        // 1) Check the value of each and every element of the array
        if(min > array[index])
        {

        // 3) if there is another minimum element of the array then replace it. else leave it
            min = array[index];
        }
        min = recursion(array, min, index+1);
        return min;
    }
}

int min_element_of_array_using_rec(int *array)
{
    // 2) let the minimum element of the array be the first element of the array
    return recursion(array, array[0], 0);
}


void main()
{
    int array[5] = {6,10,0, 100, -1};

    printf("%d",min_element_of_array_using_rec(array));

}