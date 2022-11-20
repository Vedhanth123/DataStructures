// c program to implement selection sort.

# include <stdio.h>
# include <conio.h>

// algo:    swap the smallest element in the array to the first.

// 0) start from the second place in the array
// 1) find out the smallest element in the array 
// 2) swap the smallest element in the array to the first place and element in the first place to the
// place of smallest element in the array

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void main()
{
    int array[10] = {6,2,0,1,3,4,5,8,7,9};

    int index_of_smallest_value = 0;


    // 0) start from the second place of the array
    for(int i = 1; i < 10; i ++ )
    {
        
        // 1) find out the smallest element of the array 
        for(int j = i; j < 10; j ++ )
        {
            if(array[j] < array[index_of_smallest_value])
            {
                index_of_smallest_value = j;
            }
        }

        // 2) swap the smallest element in the array to the first place and element in the first place to the
        // place of smallest element in the array
        swap(&array[i-1],&array[index_of_smallest_value]);
        
    }
    for(int i = 0; i < 10; i ++)
    {
        printf("%d\n",array[i]);
    }
    
    getch();
}
