#include <stdio.h>
#include <stdlib.h>

const int size = 4;

// declaring array for storing the data
int Array[] = {40, 30, 20, 10};

// declaring array to store the sorted array
int Sorted_array[size];

int *MergeSort(int array[], int left, int right)
{
     if (left > right)
     {
          return array;
     }

     // divide the array

     // 1) split the array into two parts

     // declaring mid to find out the mid point of the array
     int mid = (left + right) / 2;

     // declaring arrays for left and right
     static int left[mid];
     static int right[right - mid];

     int index_for_left_array = 0;
     int index_for_right_array = 0;

     int index_for_main_array = 0;
     while (index_for_left_array < mid && index_for_main_array < size)
     {
          left[index_for_left_array] = array[index_for_main_array];
     }

     
    while(index_for_right_array < (right-mid) && index_for_main_array < size)
    {
         right[index_for_right_array] = array[index_for_main_array];
    }
    
    // 2) calling left and right array for recursion
    MergeSort(left, left, mid);
    MergeSort(right, mid+1, right);

    // 3) sort the array
}