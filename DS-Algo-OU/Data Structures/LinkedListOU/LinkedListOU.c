#include <stdio.h>
#include <stdlib.h>

// create a node of struct data type to store data and link to point to node
struct node
{
    int data;
    struct node *link;
};

typedef struct node node;

// create headers for the linked list
struct node *first = NULL, *last, *n1;

// function to insert values into nodes from the last
void insert(int data)
{
    // allocating memory for the nodes
    n1 = (struct node *)malloc(sizeof(struct node));

    // inserting data into nodes
    n1->data = data;

    n1->link = NULL;

    if (first == NULL)
    {
        first = n1;
    }
    else
    {
        last->link = n1;
    }
    last = n1;
}
void randominsert(int data, int index)
{
    // create a node
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    temp->data = data;

    // creating an iterator
    int i = 0;

    // create a node for traversing the linked list
    struct node *traverser = first;

    while (i < index - 1 && traverser != NULL)
    {
        traverser = traverser->link;
        i++;
    }

    temp->link = traverser->link;
    traverser->link = temp;
}

// function to insert node before front
void insertfront(int data)
{
    // creating a node and inserting data into the node
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    temp->data = data;

    // checking if first is empty
    if (first == NULL)
    {
        // if first is empty then assign newly created node to the first pointer
        first = temp;
        temp->link = NULL;
    }
    else
    {
        // linking new created node to first
        temp->link = first;

        // reassiging newly created node as first
        first = temp;
    }
}

// Create a function to reverse a linked list
void reverse()
{
    // 1) point to the last node of the linked list
    // 2) Take the link of the last node and point it to the last node

    // Take two pointers one points to the last node
    // Another one points to the node just before the last one
    node *last = first, *just_before_last = NULL, *temp;

    while (last)
    {

        temp = last->link;
        last->link = just_before_last;

        just_before_last = last;
        last = temp;
    }
}

void randomdelete(int index)
{
    // create two pointers
    struct node *traverser = first, *temp;
    int i = 0;

    while (i < index - 1 && traverser != NULL)
    {
        traverser = traverser->link;
        i++;
    }

    temp = traverser->link;
    traverser->link = temp->link;
    free(temp);
}

void traverse()
{
    // traversing the linked list
    struct node *temp;

    temp = first;
    while (temp != NULL)
    {
        printf("%d\n", temp->data);
        temp = temp->link;
    }
}

// function to search the linked list
int search(int key)
{
    struct node *temp;

    temp = first;

    int found = 0, i;
    while (temp != NULL)
    {
        if (temp->data == key)
        {
            found = 1;
            break;
        }
        temp = temp->link;
    }

    if (found == 1)
        return i;
    else
        return -1;
}

// function to search and replace elements in the linked list
void replace(int key, int replace)
{
    struct node *temp;

    temp = first;

    int i;

    while (temp != NULL)
    {
        if (temp->data == key)
        {
            temp->data = replace;
            break;
        }
        temp = temp->link;
    }
}

void main()
{

    int i;

    printf("Inserting data into node\n");
    for (i = 1; i <= 5; i++)
        insert(i * 10);
}
