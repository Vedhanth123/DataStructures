// take an array
#include <stdio.h>

int array[10] = {9,8,7,6,5,4,3,2,1,0};

// write a function to divide the array every time into 2 parts till the size of array is 1
void MergeSort(int* array, int left, int right) { 
    
    if(left >= right) {
        return 0;
    }

    int mid = (left + right) / 2;
    MergeSort(array, left, mid);
    MergeSort(array, mid+1, right);

    int merged_sorted_array_index = 0
    
    while()

}