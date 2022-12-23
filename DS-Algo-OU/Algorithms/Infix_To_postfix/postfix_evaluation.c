#include <stdio.h>

// declaring an array to store elements of stack
int stack[10];

int sp = -1;

// pushing elements into stack
void push(int data)
{

    if (sp != 10)
    {
        // increment stack pointer
        sp++;

        // inserting data into stack
        stack[sp] = data;
    }
}
// popping elements from stack
int pop()
{
    if (sp != -1)
    {

        return stack[sp--];
    }
}

// take input of postfix string
int main()
{
    char postfix[100] = "23+";

    // Enter your string
    puts("Enter your postfix string:");
    // gets(postfix);

    int x = 0;
    int op1;
    int op2;
    while (postfix[x] != '\0')
    {
        if (postfix[x] == '0' || postfix[x] == '1' || postfix[x] == '2' || postfix[x] == '3' || postfix[x] == '4' || postfix[x] == '5' || postfix[x] == '6' || postfix[x] == '7' || postfix[x] == '8' || postfix[x] == '9')
        {
            push(((int)postfix[x]) - 48);
        }
        if (postfix[x] == '+')
        {
            op1 = pop();
            op2 = pop();
            push(op1 + op2);
        }
        if (postfix[x] == '-')
        {
            op1 = pop();
            op2 = pop();
            push(op1 - op2);
        }
        if (postfix[x] == '*')
        {
            op1 = pop();
            op2 = pop();
            push(op1 * op2);
        }
        if(postfix[x] == '/')
        {
            op1 = pop();
            op2 = pop();
            push(op1 / op2);
        }
        if(postfix[x] == '%')
        {
            op1 = pop();
            op2 = pop();
            push(op1 % op2);
        }

        x += 1;
    }

    puts(stack);
    return 0;
}