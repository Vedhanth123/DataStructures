#include <stdio.h>
#include <stdlib.h>

// create a node of struct data type to store data and link to point to node
struct node
{
    int data;
    struct node *link;
};

// create headers for the linked list
struct node *first = NULL, *last, *n1;

// function to insert values into nodes from the last
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
    while(temp != NULL)
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

    while(temp != NULL)
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
    for (i = 0; i < 5; i++)
        insert();

    printf("Printing the linked List\n");
    traverse();

    printf("Enter data to insert the node at random index\n");
    int data;
    scanf("%d",&data);
    printf("Enter your random insert value\n");
    int index;
    scanf("%d",&index);
    
    randominsert(data, index);

    printf("Deleting data randomly from the linked list\n");
    printf("Enter index in which you want to delete data at\n");
    scanf("%d", &index);

    randomdelete(index);

    printf("printing the linked list\n");
    traverse();
}
