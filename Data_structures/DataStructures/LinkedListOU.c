#include <stdio.h>
#include <stdlib.h>

// create a node of struct data type to store data and link to point to node
struct node
{
    int data;
    struct node *link;
};

int count = 0;

// create headers for the linked list
struct node *first = NULL, *last, *n1;

// function to insert values into nodes
void insert()
{
    // allocating memory for the nodes
    n1 = (struct node *)malloc(sizeof(struct node));

    // asking user to enter data into nodes
    int data;
    printf("Enter data into node:\n");
    scanf("%d", &data);

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

    // keeping track of no. of nodes by incrementing the counter
    count++;
}
void randominsert(int data, int index)
{
    // create a pointer which create a new node
    struct node *dummypointer = (struct node *)malloc(sizeof(struct node));

    // insert data into it
    dummypointer->data = data;

    // creating a counter variable which keeps track of index of the linked list
    int count = 1;

    struct node *traverser = first;
    struct node *prev = first;

    // traverse till till the index
    while (traverser != NULL && count != index)
    {
        if (index != 1)
        {
            prev = prev->link;
        }

        traverser = traverser->link;
        count++;
    }

    // address of current element must be given to the newly created node
    dummypointer->link = prev->link;
    prev->link = dummypointer;
}

void randomdelete(int index)
{
    // create two pointers
    struct node *traverser = first, *prev = first;
    int count = 1;

    while (traverser != NULL && count != index)
    {
        if (index != 1)
        {
            prev = prev->link;
        }

        traverser = traverser->link;
        count++;
    }

    prev->link = traverser->link;
    free(traverser);
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
        previous = previous->link;
    }

    // 2) delete the node in that particular place
    temp = previous->link;

    post = temp->link;

    free(temp);

    // 3) re link the previous node to the next node
    previous->link = post;

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

    for (i = 0; i < count; i++)
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

    for (i = 0; i < 5; i++)
        insert();

    traverse();

    randominsert(4, 2);
    randomdelete(5);

    traverse();
}
