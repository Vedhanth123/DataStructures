#include <stdio.h>
#include <stdlib.h>

// create a struct
struct node
{
    int data;
    struct node *link;
};

// creating nick name for the struct node as node
typedef struct node node;

node *r = NULL;

// creating function to create memory using structure
node *getNode()
{
    // creating a temporary variable to allocate memory
    node *temp = (node *)malloc(sizeof(node));
    temp->link = NULL;
    return temp;
}

// creating a function insert node at start
void ins(node *s, int data)
{
    // allocating node
    node *temp = getNode();

    // adding data to node
    temp->data = data;

    // linking with another node
    s->link = temp;
}

// function to create a node and assigning 
void create_node(int data)
{
    node *temp = getNode();
    temp->data = data;

    if (r == NULL)
    {
        r = temp;
    }
}

void main()
{
    int a = 1000;
    create_node(0);
    ins(r, a);
}