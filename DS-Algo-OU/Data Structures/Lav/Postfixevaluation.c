#include <stdio.h>

// string expression
// 1) push operand to stack
// 2) pop two operands from stack and evaluate them and push answer to stack if you encounter operator

// create a stack of char datatype
char Stack[10];
int sp = 0;

// push
void push(char x)
{
    if(sp == 10)
        printf("Overflow\n");
    else
        Stack[sp++];
}
char pop()
{
    if(sp == -1)
        printf("Underflow\n");
    else
        return Stack[--sp];
}


int evaluate(char *expression)
{
    char *p;

    while(*p != '\0')
    {
        if(*p == '+' || *p == '-' || *p == '*' || *p == '/')
        {
            char o1 = pop();
            char o2 = pop();

            if(*p == '+')
                push(((int)o1 - 48)  + ((int)o2 - 48));
            if(*p == '*')
                push(((int)o1 - 48)  * ((int)o2 - 48));
            if(*p == '-')
                push(((int)o1 - 48)  - ((int)o2 - 48));
            if(*p == '/')
                push(((int)o1 - 48)  / ((int)o2 - 48));
        }
        else
        {
            push(*p);
        }
        p++;
    }
    return pop();
}
int main()
{
    char [3] = "23+";

    printf("%c",evaluate());
    return 0;
}