#include <stdio.h>
#include <conio.h>

void main()
{
    
    int array[5] = {4,10,40,6,8};
    
    // asking user for the key
    int key;
    printf("Enter the number which you want to search in the array:\n");
    scanf("%d",&key);

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
