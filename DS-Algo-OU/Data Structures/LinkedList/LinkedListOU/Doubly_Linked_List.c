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
struct node *head = NULL;
struct node *prev = NULL;

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
        return;
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

void traverse()
{
    struct node *temp = head;
    while(temp != NULL)
    {
        printf("%d ", temp->data);
        temp = temp->right;
    }
    printf("\n");
}
// function to delete the node from end
void delete_from_end()
{
    struct node *temp = prev;
    prev = prev->left;
    prev->right = NULL;
    free(temp);
}

void delete_from_start()
{
    struct node *temp = head;
    head = head->right;
    head->left = NULL;
    free(temp);
}

void random_delete(int index)
{
    struct node *t = head;
    int c= 0;
    struct node *l = t->right->right;
    while(t != NULL && c != index && l != NULL)
    {
        t = t->right;
        l = l->right;
        c ++;
    }
    l->left->left = t;
    free(t->right);
    t->right = l;
}

void main()
{
    insert_at_end(100);
    traverse();
    insert_at_end(200);
    traverse();
    insert_at_end(300);
    traverse();
    insert_at_head(50);
    traverse();
    insert_at_random(150, 1);
    traverse();
    delete_from_end();
    traverse();
    delete_from_start();
    traverse();
    random_delete(2);
    traverse();
}