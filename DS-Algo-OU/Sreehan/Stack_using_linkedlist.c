#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct node *ptr;
};

struct Node *head = NULL, *tail = NULL, *newnode;

// stack: push pop
// push
void push(int data)
{
    // create a node
    newnode = (struct Node *)malloc(sizeof(struct Node));
    newnode->data = data;

    if (head == NULL)
    {
        head = newnode;
        tail = newnode;
    }
    else
    {
        newnode->ptr = head;
        head = newnode;
    }
}
void pop()
{
    if (head == NULL)
    {
        printf("Stack Underflow!\n");
    }
    else
    {
        struct node *temp = head;
        printf("%d", head->data);
        head = head->ptr;
        free(temp);
    }
}
void display()
{
    struct Node *temp = head;
    while (temp != NULL)
    {
        printf("%d", temp->data);
        temp = temp->ptr;
    }
}
void main()
{
    int stopper = 1;
    int choice;
    int val;

    while (stopper != 0)
    {
        printf("Enter your choice: \n");
        printf("Enter 1 for push:\nEnter 2 for pop\nEnter 3 for display:\nEnter 4 for exit:");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Enter value whcih you want to push:\n");
            scanf("%d", &val);
            push(val);
            break;
        case 2:
            pop();
            break;
        case 3:
            display();
            break;
        case 4:
            stopper = 0;
            break;
        default:
            printf("Invalid option entered!\n");
        }
    }
}