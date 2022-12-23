#include <stdio.h>
#include <stdlib.h>

// create a doubly linked list
struct node
{
    int data;
    struct node *left;
    struct node *right;
}; 

// pointer to store first node of the linked list
struct node *head;
struct node *prev;

// function to add nodes at last
void *insert_at_end(int data)
{
    // create a node
    struct node *n1 = (struct node*) malloc(sizeof(struct node));

    // inserting data into the node
    n1->data = data;

    n1->right = NULL;

    if(head == NULL)
    {
        head = n1;
        n1->left = NULL;
    }
    
    else
    {
        prev->right = n1;
        n1->left = prev;
    }
    prev = n1;

}

// function to add a node at head
void insert_at_head(int data)
{
    // create a node
    struct node *n1 = (struct node*) malloc(sizeof(struct node));

    // inserting data into the node
    n1->data = data;

    n1->right = head;
    n1->left = NULL;

    head->left = n1;
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

void reverse()
{
    struct node *temp = head;

    while(temp)
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