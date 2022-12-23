#include <iostream>
using namespace std;

// function to sort and Merge the two arrays
void Merge(int array[], int left, int mid, int right)
{
    // creating the size of array
    int left_size = mid - left + 1;
    int right_size = right - mid;

    // creating two arrays
    int *left_array = new int[left_size];
    int *right_array = new int[right_size];

    // adding elements to the two arrays
    for(int i = 0; i < left_size; i ++)
    {
        left_array[i] = array[left + i];
    }
    for(int j = 0; j < right_size; j ++)
    {
        right_array[j] = array[left + left_size+j];
    }

    // creating indexes of left, right and array
    int left_array_index = 0;
    int right_array_index = 0;
    int main_array_index = left;

    // sorting the array
    while(left_array_index < left_size && right_array_index < right_size)
    {
        if(left_array[left_array_index] <= right_array[right_array_index])
        {
            array[main_array_index] = left_array[left_array_index];
            main_array_index += 1;
            left_array_index += 1;
        }
        else
        {
            array[main_array_index] = right_array[right_array_index];
            main_array_index += 1;
            right_array_index += 1;
        }
    }
    while(left_array_index < left_size)
    {
        array[main_array_index] = left_array[left_array_index];
        main_array_index += 1;
        left_array_index += 1;
    }
    while(right_array_index < right_size)
    {
        array[main_array_index] = right_array[right_array_index];
        main_array_index += 1;
        right_array_index += 1;
    }
}

// function to divide the array into two parts
void MergeSort(int array[], int left, int right)
{
    if(left < right)
    {
        int mid = (left + (right) - 1) / 2;

        MergeSort(array, left, mid);
        MergeSort(array, mid+1, right);

        Merge(array, left, mid, right);
    }
}

int main()
{
    int array_to_sort[5] = {9,8,7,6,5};
    MergeSort(array_to_sort, 0, 4);
    for(int i = 0; i < 5; i ++)
    {
        cout << array_to_sort[i];
    }

}