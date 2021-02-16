#include <stdio.h>
#include <stdlib.h>
#include <conio.h>


// circular linked list

struct node
{
    int data;
    struct node *link;
};

typedef struct node node;

node *first = NULL;
node *last;
node *new_node;

int counter;

void insert()
{
    
    int data;
    printf("Enter data into nodes:\n");
    scanf("%d",&data);
    
    new_node  = (node*) malloc(sizeof(node));

    new_node->data = data;

    if(first == NULL)
    {
        first = new_node;
        new_node->link = new_node;
    }
    else
    {
        last->link = new_node;
    }
    last = new_node;
    last->link = first;

    counter ++;

}

void display()
{
    node *temp;

    for(int i = 0; i < counter; i++)
    {
        printf("%d\n",temp->data);
        temp = temp->link;
    }
}

void main()
{
    int i;
    
    for(i = 0; i < 5; i ++)
        insert();
    
    getch();
}
