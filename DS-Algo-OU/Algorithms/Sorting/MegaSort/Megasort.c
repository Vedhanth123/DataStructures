// Quick sort in C

#include <stdio.h>

// function to swap elements
void swap(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int arr[5] = {5,4,3,2,1};

// quicksort -----------------------------------------------------------------------------
int partition(int arr[], int low, int high)
{

    int pivot = arr[high];

    int i = (low - 1);

    for (int j = low; j < high; j++)
    {
        if (arr[j] <= pivot)
        {

            i++;

            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[high]);

    return (i + 1);
}

void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {

        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);

        quickSort(arr, pi + 1, high);
    }
}

// selection sort -----------------------------------------------------------------------
void selectionSort(int arr[], int size)
{
    for (int step = 0; step < size - 1; step++)
    {
        int min_idx = step;
        for (int i = step + 1; i < size; i++)
        {

            if (arr[i] < arr[min_idx])
                min_idx = i;
        }

        swap(&arr[min_idx], &arr[step]);
    }
}

// Mergesort -------------------------------------------------------------------------------

void merge(int arr[], int p, int q, int r)
{

    int n1 = q - p + 1;
    int n2 = r - q;

    int L[n1], M[n2];

    for (int i = 0; i < n1; i++)
        L[i] = arr[p + i];
    for (int j = 0; j < n2; j++)
        M[j] = arr[q + 1 + j];

    int i, j, k;
    i = 0;
    j = 0;
    k = p;

    while (i < n1 && j < n2)
    {
        if (L[i] <= M[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = M[j];
            j++;
        }
        k++;
    }

    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2)
    {
        arr[k] = M[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int l, int r)
{
    if (l < r)
    {

        int m = l + (r - l) / 2;

        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        merge(arr, l, m, r);
    }
}

// insertion sort ---------------------------------------------------------------------------------------------------

void insertionsort(int arr[])
{
    for (int i = 0; i < 5; i++)
    {
        for (int j = 1; j < 5; j++)
        {
            if (arr[j - 1] > arr[j])
            {
                swap(&arr[j - 1], &arr[j]);
            }
        }
    }
}

// bubble sort ------------------------------------------------------------------------------------------
void bubblesort(int arr[], int len)
{
    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < len - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(&arr[j], &arr[j + 1]);
            }
        }
    }
}

// heapsort --------------------------------------------------------------------------------------------------
void heapify(int arr[], int n, int i)
{
    // Find largest among root, left child and right child
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    // Swap and continue heapifying if root is not largest
    if (largest != i)
    {
        swap(&arr[i], &arr[largest]);
        heapify(arr, n, largest);
    }
}

// Main function to do heap sort
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

void printarr(int arr[], int size)
{
    for (int i = 0; i < size; ++i)
    {
        printf("%d  ", arr[i]);
    }
    printf("\n");
}


void main()
{
    // heapsort
    int arr[5] = {5,4,3,2,1};
    printf("Before Heapsort:\n");
    printarr(arr, 5);
    heapSort(arr, 5);
    printf("After Heapsort:\n");
    printarr(arr, 5);

    // Mergesort
    int arr1[5] = {5,4,3,2,1};
    printf("Before Mergesort:\n");
    printarr(arr1, 5);
    mergeSort(arr1, 0, 4);
    printf("After Mergesort:\n");
    printarr(arr1, 5);

    // selection sort
    int arr2[5] = {5,4,3,2,1};
    printf("Before Selection sort:\n");
    printarr(arr2, 5);
    selectionSort(arr2, 5);
    printf("After selection sort:\n");
    printarr(arr2, 5);

    // insertion sort
    int arr3[5] = {5,4,3,2,1};
    printf("Before Insertion sort:\n");
    printarr(arr3, 5);
    insertionsort(arr3);
    printf("After Insertion sort:\n");
    printarr(arr3, 5);

    // bubble sort
    int arr4[5] = {5,4,3,2,1};
    printf("Before bubble:\n");
    printarr(arr4, 5);
    bubblesort(arr4, 5);
    printf("After Mergesort:\n");
    printarr(arr4, 5);

    // quick sort
    int arr5[5] = {5,4,3,2,1};
    printf("Before quick sort:\n");
    printarr(arr5, 5);
    quickSort(arr5, 0, 4);
    printf("After quick sort:\n");
    printarr(arr5, 5);

}