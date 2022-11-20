#include<stdio.h>
#include <conio.h>

int Merge(int array[], int left, int mid, int right)
{
    // preparing the size of two temp arrays 
    int tl = mid - left + 1, tr = right - mid;

    // creating two temp arrays to store the values 
    int left_temp[tl], right_temp[tr];

    // copying elements from array to temp arrays
    for(int i = 0; i < tl; i ++)
    {
        left_temp[i] = array[left+i];
    }

    for(int j = 0; j < tr; j++)
    {
        right_temp[j] = array[left+tl+j];
    }

    // sorting and merging the arrays into one array
    int merged_and_sorted_array_index = left;
    int left_array_index = 0;
    int right_array_index = 0;

    while(left_array_index < tl && right_array_index < tr)
    {
        if(left_temp[left_array_index] <= right_temp[right_array_index])
        {
            array[merged_and_sorted_array_index] = left_temp[left_array_index];
            left_array_index += 1;
            merged_and_sorted_array_index += 1;
        }
        else
        {
            array[merged_and_sorted_array_index] = right_temp[right_array_index];
            right_array_index += 1;
            merged_and_sorted_array_index += 1;
        }
    }

    // copy the remaining elements to the array
    while(left_array_index < tl)
    {
        array[merged_and_sorted_array_index] = left_temp[left_array_index];
        left_array_index += 1;
        merged_and_sorted_array_index += 1;
    }

    while(right_array_index < tr)
    {
        array[merged_and_sorted_array_index] = right_temp[right_array_index];
        right_array_index += 1;
        merged_and_sorted_array_index += 1;
    }

}

int Merge_sort(int array[], int left, int right)
{
    if(left >= right)
    {
        return 0;
    }

    int mid = (left+(right-1))/2;

    // Splitting left side of array
    Merge_sort(array, left, mid);

    // Splitting right side of array
    Merge_sort(array, mid+1, right);

    // Merging two arrays and as well as sorting them out
    Merge(array, left, mid, right);

}

void main()
{
    int array[6] = {5,4,3,2,1,0};

    Merge_sort(array, 0, 5);

    for(int i = 0; i < 6; i++)
        printf("%d\n",array[i]);
    
    getch();
}
