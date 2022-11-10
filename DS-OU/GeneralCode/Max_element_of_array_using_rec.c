#include <stdio.h>

// To find the max element of the array

// 1) Check the value of each and every element of the array
// 3) if there is another maximum element of the array then replace it. else leave it
// 4) continue the process till you reach the last index of the array

int max_element_of_array_using_rec(int *array);
int recursion(int *array, int max, int index);

int recursion(int *array, int max, int index)
{
    // 4) continue the process till you reach the last index of the array
    if(index == 5)
    {
        return max;
    }
    else
    {
        // 1) Check the value of each and every element of the array
        if(max < array[index])
        {

        // 3) if there is another maximum element of the array then replace it. else leave it
            max = array[index];
        }
        max = recursion(array, max, index+1);
        return max;
    }
}

int max_element_of_array_using_rec(int *array)
{
    // 2) let the maximum element of the array be the first element of the array
    return recursion(array, array[0], 0);
}


void main()
{
    int array[5] = {6,10,0, 100, -1};

    printf("%d\n",max_element_of_array_using_rec(array));

}