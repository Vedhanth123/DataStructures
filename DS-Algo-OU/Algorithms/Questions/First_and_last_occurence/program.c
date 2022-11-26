#include <stdio.h>

int array[6] = {1, 2, 1, 1, 5, 2};

int left_to_right(int *array, int index, int key)
{
    if (index == 6)
    {
        return 0;
    }
    if (array[index] == key)
    {
        printf("First occurence at %d, ", index);
        return index;
    }
    else
    {
        left_to_right(array, index + 1, key);
    }
}

int right_to_left(int *array, int index, int key)
{
    if (index == -1)
    {
        return 0;
    }
    if (array[index] == key)
    {
        printf("Last occurence at %d, ", index);
        return index;
    }
    else
    {
        right_to_left(array, index - 1, key);
    }
}
int main()
{
    left_to_right(array, 0, 1);
    right_to_left(array, 5, 1);
    return 0;
}