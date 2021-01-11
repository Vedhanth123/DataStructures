#include <stdio.h>
#include <stdlib.h>

// 1) inserting / appending  [completed]
// 2) deleting / pop         [completed]
// 3) sizeof list            [completed]
// 4) traversal              [completed]
// 5) finding
// 6) sorting

// 0) LINKED LIST

// create a node containing two values 1) data 2) link to another node
struct node
{
    int data;
    struct node *pointer;
};

typedef struct node node;

// create a node
node *n1, *first = NULL, *last = NULL;

// creating a variable to keep track of size of linked list
int sizeof_list = 0;

void insert(int data)
{
    if(first == NULL)
    {
        n1 = (node*) malloc(sizeof(node));
        
        // assigning value to n1
        n1->data = data;

        n1->pointer = NULL;

        // linking first node to first
        first = n1;

        // linking first node to last
        last = n1;

        sizeof_list += 1;
    }

    else
    {
        n1 = (node*) malloc(sizeof(node));

        // assigning value to n1
        n1->data = data;

        // newly created node points to nothing
        n1->pointer = NULL;

        // previous node points to this node
        last->pointer = n1;

        // updating the last node
        last = n1;

        sizeof_list += 1;
        
    }

}

void traverse()
{
    node *traverser;

    traverser = first;
    
    for(int i = 0; i < sizeof_list; i++)
    {
        printf("%d, ",traverser->data);
        traverser = traverser->pointer;
    }
    
}

void delete()
{
    // deleting last element
    free(n1);

    // decrementing sizeof_list by 1
    sizeof_list -= 1;

    // traversing list and finding out last element
    node *temp = first;

    for(int i = 0; i < sizeof_list - 1; i ++)
    {
        temp = temp->pointer;
    }

    // inserting last node after deleting into last var

    n1 = temp;

    last = temp;   
}

void main()
{
    int increment = 10;

    for(int i = 0; i < 10; i++)
    {
        insert(increment);
        increment += 10;
    }

    for(int i = 0; i < 5; i++)
        delete();

    traverse();


}



