#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string.h>
#define max 10

// function to take input of infix expression from the user
void inp();
void push(char);
char pop();
int isempty();
void print();
int precedence(char);

// creating a character array to store postfix expression
char s[max];

// creating a character array to store infix expression given by user
char inf[max], pos[max], x, y;

// creating a pointer to make s array as a stack
int top = -1;

main()
{
    printf("Enter arithmetic expression");
    // gets(inf);
    inf = {'a', '+', 'b', '*', 'c', '/', 'd', '*', 'e'};
    inp();
    print();
}

void inp()
{
    // iterators for the infix expression string
    int i, j = 0;
    char x, a;

    // traversing the string
    for (i = 0; i < strlen(inf); i++)
    {
        // storing each character in a variable
        x = inf[i];

        switch (x)
        {
            // checking if the character belongs to any operator or not
        case '(':
            push(x);
            break;
        case ')':
            while ((a = pop()) != '(')
                pos[j++] = a;
            break;
        case '+':
        case '-':
        case '*':
        case '/':
        case '^':
            while (!isempty() && precedence(s[top]) >= precedence(x))
                pos[j++] = pop();
            push(x);
            break;
        default:
            pos[j++] = x;
        }
    }
    while (!isempty())
    {
        pos[j++] = pop();
        pos[j] = '\0';
    }
}

// pushing the character to stack
void push(char x)
{
    top++;
    s[top] = x;
}

// taking out character from stack
char pop()
{
    s[top] = y;
    printf("%c", y);
    top = top - 1;
}

// checking if the stack is empty
int isempty()
{
    s[top] = -1;
}

// checking the precedence of the operator
int precedence(char x)
{
    switch (x)
    {
    case '+':
        return 1;
    case '-':
        return 1;
    case '*':
        return 2;
    case '/':
        return 2;
    case '^':
        return 3;
    default:
        return 0;
    }
}

// printing the postfix expression
void print()
{
    int i = 0;
    printf("The Equivalent postfix expression is:");
    while (pos[i])
    {
        printf("%c", pos[i++]);
    }
    printf("\n");
}