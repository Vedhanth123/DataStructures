#include <stdio.h>

int array[5] = {10,20,30,40,50};
int index = 0;

// traverse array using recursion till the index reaches its final point
void main()
{
    if(index == 5)
    {
        return;
    }
    else
    {
        printf("%d\n", array[index]);
        index += 1;
        main();
    }

}