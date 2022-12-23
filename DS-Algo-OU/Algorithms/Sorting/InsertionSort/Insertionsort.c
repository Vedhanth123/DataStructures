#include <stdio.h>

// create a list
int array[5] = {5, 4, 3, 2, 1};

// insertion sort:
// 1) start from the 1st element of the array
// 2) check if the 2nd element of the array is smaller than the first element.
// 3) if the element is smaller than the previous one swap it
// 4) else continue

int swap(int j, int k)
{
    int temp = array[j];
    array[j] = array[k];
    array[k] = temp;
}

void insertionsort()
{
    for (int i = 0; i < 5; i++)
    {
        for (int j = 1; j < 5; j++)
        {
            if (array[j - 1] > array[j])
            {
                swap(j-1, j);
            }
        }
    }
}

int main()
{
    insertionsort();
}