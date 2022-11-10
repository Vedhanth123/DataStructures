// Stack using array
#include <stdio.h>
#include <conio.h>


// declaring an array to store elements of stack
int stack[10];

int sp = -1;

// pushing elements into stack
void push()
{

    if(sp != 10)
    {
        // ask user for data to push into stack
        int data;
        printf("Enter data to push into stack :\n");
        scanf("%d",&data);

        // increment stack pointer
        sp ++;

        // inserting data into stack
        stack[sp] = data;
    }
}
// popping elements from stack
void pop()
{
    if(sp != -1)
    {

        printf("%d\n",stack[sp]);
        stack[sp] = 0;
        
        sp --;
    }

}
 

void main()
{
    for(int i = 0; i < 10; i ++)
    {
        push();
    }
    for(int i = 0; i < 10 ; i++)
    {
        pop();
    }

    getch();
}
