#include <stdio.h>

// program to access variable using pointer
void main()
{
    // creating a normal variable
    int var = 10;

    // declaring a pointer variable
    int *pointer;

    // inserting address of normal variable into pointer
    pointer = &var;

    // printing address of variable using pointer and variable itself
    printf("%u with pointer, %u with variable itself\n", pointer, &var);

    // printing value at address using pointer and varialbe itself
    printf("%d with pointer, %d with variable itself\n", *pointer, var);

    // 19124-CM-111 Vedhanth

}