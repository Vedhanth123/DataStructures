#include <stdio.h>
#include <stdlib.h>

// To find duplicates in an array
struct Dict
{
    int data;
    int no_of_copies;
    struct Dict *pointer;
};

struct Dict *head, *next, *dummynode;

void insert(int data)
{
    dummynode = (struct Dict *)malloc(sizeof(struct Dict));
    dummynode->data = data;
    dummynode->no_of_copies = 0;
    dummynode->pointer = NULL;

    if (head == NULL)
    {
        head = dummynode;
    }
    else
    {
        next->pointer = dummynode;
    }
    next = dummynode;
}

void search(int data)
{
    dummynode = head;
    int found = 0;
    while (dummynode != NULL)
    {
        if (dummynode->data == data)
        {
            found = 1;
            dummynode->no_of_copies += 1;
        }
        dummynode = dummynode->pointer;
    }
    
    if(found == 0)
    {
        insert(data);
        search(data);
    }
    
}

void traverse()
{
    dummynode = head;
    while(dummynode != NULL)    
    {
        printf("%d: %d\n",dummynode->data, dummynode->no_of_copies);
        dummynode = dummynode->pointer;
    }
}

int main()
{
    int array1[] = {1, 2, 3, 1, 2, 2,2,2,2,2,2,2,2,1000, 2,2,55,5,5,5,5,5,5,1000, -1, 0, 2,3,5,3,1,5,9, 100, 90, 290, 5900};

    // Let us create a data structure which stores the value as well as how many copies it has
    for (int i = 0; i < sizeof(array1)/sizeof(int); i++)
    {
        search(array1[i]);
    }

    traverse();
}