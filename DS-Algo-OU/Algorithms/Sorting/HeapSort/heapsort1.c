#include <stdio.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Heap definition: Heap is a type of complete binary tree.
// complete binary tree: Complete binary tree is a type of binary tree where the nodes are filled to the left side first
// Heaps are of two types: 1) Max heap 2) Min Heap
// Max heap: Max heap is a type of heap where the root is the largest element and vice versa

// formula for heap 
// left element = 2*n + 1
// right element = 2*n + 2
int arr[5] = {1,5,3,4,2};

// function to heapify the array
void heapify(int array[], int i, int n)
{
    // assume the middle element of the array as the largest element of the array
    int largest = i;
    int left = 2*i + 1;
    int right = 2*i + 2;

    if(left < n && array[left] > array[largest])
        largest = left;
    if(right < n && array[right] > array[largest])
        largest = right;
    
    if(largest != i)
    {
        swap(&array[i], &array[largest]);
        heapify(array, largest, n);
    }
    
}

void heapSort(int arr[], int n)
{
    // Build max heap
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // Heap sort
    for (int i = n - 1; i >= 0; i--)
    {
        swap(&arr[0], &arr[i]);

        // Heapify root element to get highest element at root again
        heapify(arr, i, 0);
    }
}

int main()
{
    heapSort(arr, 5);
    return 0;
}
