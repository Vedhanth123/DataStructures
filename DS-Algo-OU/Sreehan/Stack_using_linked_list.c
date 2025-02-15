#include <stdio.h>
#include <stdlib.h>
// push pop by using linked list
struct Node
{
    int data;
    struct Node *ptr;
};
struct Node *head = NULL, *tail = NULL, *newnode;

void push(int data)
{
    newnode = (struct Node *)malloc(sizeof(struct Node));
    newnode->data = data;
    if (head == NULL)
    {
        head = newnode;
    }
    else
    {
        newnode->ptr = head;
        head = newnode;
    }
}
void pop()
{
    struct Node *dummy = head;
    if (head == NULL)
    {
        printf("underflow");
        ;
    }
    else
    {
        head = head->ptr;
        printf("%d", dummy->data);
        free(dummy);
    }
}
void display()
{
    struct Node *temp=head;
    while(temp!=NULL)
    {  
        printf("%d",temp->data);
        temp=temp->ptr;
    }
}

void main()
{
    int choice;
    int value;
    while(choice!=0)
    {
        printf("1.insertion/n2.delection/n3.display/n4.exit");
        scanf("%d",&choice);
        switch(choice)
        {
            case 1:
            printf("enter your value/n");
            scanf("%d",&value);
            push(value);
            break;;
            case 2:
            pop();
            break;
            case 3:
            display();
            break;
            case 4:
            exit(0);
            default:
            printf("you have entered invaild value!");
        }
    }
}