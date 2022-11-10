// c program on linear search
#include <stdio.h>
#include <conio.h>

void main()
{   
    // 1) start from the first element of the array
    // 2) check if the element is equal to key
    // 3) if the element is not equal to key then proceed to another one
    // 4) if the element is same then break the loop


    // Best case time complexity of linear search O(1)
    // Worst case time complexity of linear search O(n)

    // Best case time complexity of binary search O(1)
    // Worst case time complexity of binary search O(logn)

    int array[5] = {4,10,40,6,8};
    
    // asking user for the key
    int key = 10;

    // checking if element found or not
    int found = 0;
    int i = 0;

    for(i = 0; i < 5; i ++)
    {
        
        if(key == array[i])
        {
            found = 1;
            break;
        }
    }
    
    if(found)
        printf("key found at %d place:\n",i+1);
    else
        printf("key not found:\n");
    
    getch();

}
