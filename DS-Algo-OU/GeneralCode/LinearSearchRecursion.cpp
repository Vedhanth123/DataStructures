#include <iostream>
using namespace std;

// reduce the array length every time you search for the array
bool linearsearch(int *array, int start, int end, int key)
{
    if(start == end)
    {
        return false;
    }
    else
    {
        if(key == array[start])
        {
            return true;
        }
        else
        {   
            linearsearch(array, start + 1, end, key);
        }
    }
}
int main()
{
    int array[5] = {5,9,2,3,0};
    int key = 0;

    cout << linearsearch(array, 0, 5, 111);
    return 0;
}