#include <stdio.h>

// 19124-CM-111 Vedhanth
void swap(int *a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}


// adjusting pivot element and making sure elements greater than pivot are left to the pivot
// elements greater than pivot are right to the pivot
int pivot_adjuster(int array[], int first, int last)
{

    // iterator i 
    int i = first - 1;


    // selecting pivot as the last element of the array
    int pivot = array[last];

    // iterating through array and finding out elements < or > pivot
    for(int j = first; j < last; j ++ )
    {
        // swapping elements and placing elements in pivotal order
        if(pivot >= array[j])
        {
            i += 1;
            swap(&array[j], &array[i]);
        }
    }

    // adjusting the pivot
    swap(&array[last],&array[i+1]);

    // returning the placement of the pivot
    return i + 1;
    
}

int QuickSort(int array[], int first, int last)
{

    // base case of recursion
    if(first >= last)
    {
        return 0;
    }

    int pivot = pivot_adjuster(array, first, last);

    // sorting the left part of the array and not including the pivot element as that
    // is already in correct place

    QuickSort(array, first, pivot-1);

    // sorting the right part of the array not including pivot
    QuickSort(array, pivot+1, last);

}

int main()
{

    // 1) set pivot as the last element of the array
    // 2) arrange elements less than pivot to the left of the pivot and greater than pivot to right of the pivot
    // 3) adjust pivot location
    
    int array[5] = {5,4,3,2,1};

    QuickSort(array, 0, 4);

    // printing the array
    for(int i = 0; i < 5; i ++ )
    {
        printf("%d\n",array[i]);
    }

    return 0;

}
