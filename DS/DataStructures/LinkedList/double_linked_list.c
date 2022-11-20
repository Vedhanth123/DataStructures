#include <stdio.h>
#include <stdlib.h>
#include <conio.h>


// double linked list creation

struct node
{
    int data;
    struct node *p1;
    struct node *p2;
};

typedef struct node node;

// dummy headers
node *first = NULL;
node *last;
node *new_node;
node *previous = NULL;

void insert()
{
    // allocation of memory
    new_node = (node*) malloc(sizeof(node));

    // asking user for data
    int data;
    printf("Enter data :\n");
    scanf("%d",&data);

    new_node->data = data;

    new_node->p2 = NULL;

    new_node->p1 = previous;

    if(first == NULL)
    {
        first = new_node;
    }
    else
    {
        last->p2 = new_node;
    }

    last = new_node;
    previous = new_node;

}

void travese()
{

    struct node *temp;

    while(temp->p2 != NULL)
    {
        printf("%d\n",temp->data);
        temp = temp->p2;
    }

}

void main()
{
    int i;
    
    for(int i = 0 ; i < 5; i++)
    {
        insert();
    }

    travese();

    getch();
}
