#include <stdio.h>
#include <stdlib.h>

// create a structure
struct node
{
    int data;
    struct node *left;
    struct node *right;
};

struct node *head, *last;

// function to add nodes at last
void insert_at_end(int data)
{
    // creating memory
    struct node *n1 = (struct node*) malloc(sizeof(struct node));

    // inserting data into the nodes
    n1->data = data;

    if(head == NULL)
    {
        head = n1;
        n1->left = head;
    }
    else
    {
        last->right = n1;
        n1->left = last;
    }
    last = n1;
    n1->right = head;
}


// function to add a node at head
void insert_at_head(int data)
{
    // create a node
    struct node *n1 = (struct node*) malloc(sizeof(struct node));

    // inserting data into the node
    n1->data = data;

    // checking if head is null
    if(head == NULL)
    {
        head = n1;
        n1->left = head;
        n1->right = head;
        return 0;
    }


    n1->right = head;
    n1->left = last;

    head->left = n1;
    last->right = n1;

    head = n1;
}

// function to add a node at random position
void insert_at_random(int data, int index)
{   

    if(index == 0)
    {
        insert_at_head(data);
        return 0;
    }
    
    // create a node
    struct node *n1 = (struct node*) malloc(sizeof(struct node));

    // inserting data into the node
    n1->data = data;

    if(head == NULL)
    {
        head = n1;
        n1->left = head;
        n1->right = head;
        return 0;
    }

    // creating a pointer to traverse to that location
    struct node *traverser = head;

    // creating a counter
    int counter = 0;

    while(traverser && counter < index-1)
    {
        traverser = traverser->right;
        counter += 1;
    }

    // first adding address of the next node to the newly created node
    n1->right = traverser->right;

    // adding the address of the previous node to the left pointer of the n1
    n1->left = traverser;

    // adding the address of n1 to the left pointer of the next block
    traverser->right->left = n1;

    // adding the address of n1 to the right pointer of the next block
    traverser->right = n1;

}

void main()
{
    for(int i = 1; i <= 2; i ++)
    {
        insert_at_end((i*10));
    }
    for(int i = 1; i <= 2; i ++)
    {
        insert_at_random((i * 100), 0);
    }
    for(int i = 1; i <= 2; i ++)
    {
        insert_at_random((i * 1000), 3);
    }
}