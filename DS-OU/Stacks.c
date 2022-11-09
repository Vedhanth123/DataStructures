#include <stdio.h>
#include <stdlib.h>

// declare array for stacks
int Stack[10];

// create a stack pointer which points if the stack is full or empty
int sp = 0;

// function to push elements into stack
void push(int a)
{
    // checking for overflow condition
    if (sp >= 10)
    {
        printf("Stack in overflow condition: \n");
    }
    else
    {
        Stack[sp] = a;
        sp += 1;
    }
}
// functions to pop elements out from stack
void pop()
{
    // checking for underflow condition
    if (sp < 0)
    {
        printf("Stack in underflow condition: \n");
    }
    else
    {
        printf("Element to be popped out from stack: %d\n", Stack[sp]);
        Stack[sp] = NULL;
        sp -= 1;
    }
}

void main()
{
}