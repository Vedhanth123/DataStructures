#include <stdio.h>

struct Stack
{
    int data;
    struct Stack *link;
};

typedef struct Stack Stack;

Stack *top = NULL;

void push(int data)
{
    // create a new node
    Stack *newnode = (Stack*) malloc(sizeof(Stack));

    // insert data into the node
    newnode->data = data;
    newnode->link = top;

    top = newnode;
}

void pop()
{
    if(top != NULL)
    {
        Stack *temp = top;
        top = top->link;
        free(temp);
    }
    else
    {
        printf("Stack underflow");
    }
}

int main()
{
    
    for(int i = 0; i < 5; i++)
    {
        push(i*10);
    }

    for(int i = 0; i < 6; i++)
    {
        pop();
    }

    return 0;
}