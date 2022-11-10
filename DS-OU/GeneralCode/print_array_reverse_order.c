#include <stdio.h>

int array[5] = {10,20,30,40,50};
int index = -1;

// traverse array using recursion till the index reaches its final point
void main(int index)
{
    if(index == 5)
    {
        return;
    }
    else
    {
        main(index + 1);
        printf("%d\n", array[index]);
    }

}
