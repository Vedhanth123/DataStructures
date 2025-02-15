#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct node *ptr;
};

struct Node *head = NULL, *tail = NULL, *newnode;


void enque(int data)
{
    newnode = (struct Node*) malloc(sizeof(struct Node));
    newnode->data = data;

    if(head == NULL)
    {
        head = newnode;
        tail = newnode;
    }
    else
    {
        tail->ptr = newnode;
        tail = newnode;
    }
}

void deque()
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
            enque(val);
            break;
        case 2:
            deque();
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