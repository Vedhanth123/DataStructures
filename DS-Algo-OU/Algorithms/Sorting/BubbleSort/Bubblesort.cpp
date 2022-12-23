#include <iostream>
using namespace std;

// 1) sort the adjacent elements of the array if the left element is greater than the right element
// 2) keep on sorting the elements till the array is sorted
void bubblesort(int array[], int len)
{
    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < len - 1; j++)
        {
            if (array[j] > array[j + 1])
            {
                swap(array[j], array[j + 1]);
            }
        }
    }
}

int main()
{
    int array[5] = {5,4,3,2,1};

    bubblesort(array, 5);

    for(int i = 0; i < 5; i++)
    {
        cout << array[i];
    }
    return 0;
}