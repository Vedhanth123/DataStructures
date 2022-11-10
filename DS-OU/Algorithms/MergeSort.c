// take an array
#include <stdio.h>

int array[10] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};

// write a function to divide the array every time into 2 parts till the size of array is 1
void MergeSort(int *array, int left, int right)
{

    if (left >= right)
    {
        return 0;
    }

    int mid = (left + right) / 2;
    MergeSort(array, left, mid);
    MergeSort(array, mid + 1, right);

    int merged_sorted_array_index = 0;
    int swapper = 0;

    while (left < mid && mid + 1 <= right)
    {
        if (array[left] > array[right])
        {
            swapper = array[right];
            array[right] = array[left];
            array[left] = swapper;
            left++;
        }
        else
        {
            swapper = array[right];
            array[right] = array[left];
            array[left] = swapper;
            right++;
        }
    }
    if (left == mid)
    {
        while (mid + 1 <= right)
        {
        }
    }
}