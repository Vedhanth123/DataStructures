// NOT TO BE WRITTEN IN RECORD

#include <stdio.h>
#include <stdlib.h>

// create a node of struct data type to store data and pointer to point to node
struct node
{
    int data;
    struct node *pointer;
};

int count = 0;

// create headers for the linked list
struct node *first = NULL, *last, *n1;

// function to insert values into nodes
void insert(int data)
{
    // allocating memory for the nodes
    n1 = (struct node *)malloc(sizeof(struct node));

    // inserting data into nodes
    n1->data = data;

    n1->pointer = NULL;

    if (first == NULL)
    {
        first = n1;
    }
    else
    {
        last->pointer = n1;
    }
    last = n1;

    // keeping track of no. of nodes by incrementing the counter
    count++;
}

void traverse()
{
    // traversing the linked list
    struct node *temp;

    temp = first;
    // while(temp != NULL)
    // {
    //     printf("%d\n",temp->data);
    //     temp = temp->pointer;
    // }

    for (int i = 0; i < count; i++)
    {
        printf("%d\n", temp->data);
        temp = temp->pointer;
    }
}

// function to delete specific element from the list
void delete (int index)
{
    // ALGO:

    // 1) traverse through linked list and reach the position you want to delete
    // deleting nodes from the linked list
    struct node *temp, *previous, *post;

    previous = first;

    for (int i = 0; i < index - 1; i++)
    {
        previous = previous->pointer;
    }

    // 2) delete the node in that particular place
    temp = previous->pointer;

    post = temp->pointer;

    free(temp);

    // 3) re link the previous node to the next node
    previous->pointer = post;

    // keeping track of no. of nodes by decrementing the counter
    count--;
}

// function to search the linked list
int search(int key)
{
    struct node *temp;

    temp = first;

    int found = 0, i;

    for (i = 0; i < count; i++)
    {
        if (temp->data == key)
        {
            found = 1;
            break;
        }
        temp = temp->pointer;
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

    for (i = 0; i < count; i++)
    {
        if (temp->data == key)
        {
            temp->data = replace;
            break;
        }
        temp = temp->pointer;
    }
}
void reverse()
{
    struct node *temp, *prev = NULL, *next;

    temp = first;

    while(temp != NULL)
    {
        next = temp->pointer;

        temp->pointer = prev;

        prev = temp;

        temp = next;
    }

}

void main()
{
    for (int i = 0; i < 5; i++)
    {
        insert(i * 10);
    }

    reverse
}
