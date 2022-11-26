#include <stdio.h>

int array[5] = {1,2,3,4,5};
int array2[5] = {5,4,2,1,5};

// write a function to check if the array is sorted or not
int sorted_or_not(int x, int *array)
{
    if(x > 5-2) 
    {
        return 1;
    }

    if(array[x] < array[x+1])
    {
        return sorted_or_not(x + 1, array);
    }
    else
    {
        return 0;
    }
}
int main()
{
    printf("%d\n",sorted_or_not(0, array));
    printf("%d\n",sorted_or_not(0, array2));
    return 0;
}