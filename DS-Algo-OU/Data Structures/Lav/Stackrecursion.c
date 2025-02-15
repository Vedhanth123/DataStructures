#include <stdio.h>

// --------------------------- Algorithm -----------------------------------------
// Stacks using arrays -> context of the program / title of the program
// 1) Create an array
// 2)
// --------------------------------------------------------------------------------

// ----------------------------- Program -------------------------------------------
// 1) Create an array
// <datatype> array_name[size] --> syntax;
int Stack[5];
int size = 5; // -> variable initialization -> variable lo oka value insert cheyadam

// 2) create a variable to count/point to the indexes of the stack
// <datatype> variableName;
int sp = 0;

// 3) insert data into stack
// create a function to insert data into the stack -> to do repeated tasks
// function -> 1) declaration 2) definition 3) calling
// 1) declartion is not used by me
// 2) definition: we write what a function is supposed to do.
// 3) calling: we use that function whenever necessary.
// function syntax -> <returntype> function_name(datatype parameter1, datatype parameter2 ...)
// void is equal to nothing
void push(int data)
{
    // condition: 1) if 2) if-else 3) if-elseif-else 4) switch case
    // if syntax: if(condition)
    //{
    //     statements/orders/requests/code
    //}
    // = is used to insert somevalue to a variable
    if (sp == size) // == is used to check if two things are equal or not
    {
        // print the stack is full
        printf("Stack is full!\n");
    }
    else
    {
        // if stack is not full then insert data into stack
        Stack[sp] = data;
        sp++; // increments by 1
    }
}

int pop()
{
    if (sp == -1)
    {
        printf("Stack is empty:\n");
    }
    else
    {
        sp--;
        Stack[sp] = 0;
    }
}

// To stop recursion: we use return keyword
// To stop iteration: we use break keyword
// To pass iteration: we use continue keyword

// recursions are of two types: 1) head recursion 2) tail recursion
// head recursion: we write whatever code to be repeated before the termination condition
// tail recursion: we write whatever code to be repeated after ther termination condition
void rec(int a, int i)
{
    // 1) termination condition
    if(a == 5)
    {
        return;
    }
    // 2) recursive call
    else
    {
        push(i * 10);
        rec(a+1, i+1);
    }
}
int main()
{
    // function calling;
    // syntax: function_name(value);

    rec(0,1);
    
    return 0;
}