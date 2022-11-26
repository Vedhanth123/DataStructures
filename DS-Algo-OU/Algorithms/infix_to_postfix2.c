#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string.h>
#define max 10
void inp();
void push(char);
char pop();
int isempty();
void print();
int precedence(char);
char s[max];
char inf[max], pos[max], x, y;
int top = -1;
main()
{
    printf("Enter arithmetic expression");
    gets(inf);
    inp();
    print();
}
// infix to postfix function//
void inp()
{
    int i, j = 0;
    char x, a;
    for (i = 0; i < strlen(inf); i++)
    {
        x = inf[i];
        switch (x)
        {
        case '(':
            push(x); // pushs elements after ( to infix array//
            break;
        case ')':
            while ((a = pop()) != '(') // pops all the elements before ) from infix array//
                pos[j++] = a;          // all poped elements are stored in postfix array//
            break;x
        case '+':
        case '-':
        case '*':
        case '/':
        case '^':
            while (!isempty() && precedence(s[top]) >= precedence(x))
                //**if infix array is not equal to null and precedence
                // and top elemente of stack is greater than precedence of x
                // then pop it from postfix array and push it to stack
                pos[j++] = pop();
            push(x);
            break;
        default:
            pos[j++] = x;
        }
    }
    while (!isempty())
    { // otherwise postfix elements are poped till j=null//
        pos[j++] = pop();
        pos[j] = '\0';
    }
}
// push function
void push(char x)
{
    top++;
    s[top] = x;
}
// pop function
char pop()
{
    s[top] = y;
    printf("%c", y);
    top = top - 1;
} // empty function to check stack is empty or not//
int isempty()
{
    s[top] = -1;
}
// function to check precedence//
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
// function to print postfix elements
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