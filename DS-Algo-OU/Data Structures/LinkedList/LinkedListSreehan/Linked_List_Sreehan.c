#include <stdio.h>
#include <stdlib.h>

// Que: What do you want?
// Ans: I want to create a Linked List

// assignment opertors:
// 1) =
// 2) +=
// 3) -=
// 4) *=
// 5) /=
// 6) %=

// To store multiple data types in it
struct Node
{
    int data;
    struct Node *pointer; // THis is used to store the address of another node
};

// NOTE: we use -> when we are dealing with pointer to structure

// We are nick naming the struct Node -> node
typedef struct Node node;

// 1) We need to store head of linked list
node *head = NULL;

// 2) We need to create new nodes
node *newnode = NULL;

// 3) We need to link new nodes
node *linker = NULL;

// Insert from end
void insertfromend(int data)
{
    // Now lets create a node
    newnode = (node *)malloc(sizeof(node));

    // Let's insert data into node
    newnode->data = data;
    newnode->pointer = NULL;

    // Let's initialize the head if and only if head is empty
    if (head == NULL)
    {
        head = newnode;
    }
    else
    {
        // This is used to link previous node to new node by storing the address
        linker->pointer = newnode;
    }

    // Updating the linker to newnode
    linker = newnode;
}
void insertfromfront(int data)
{
    // Now lets create a node
    newnode = (node *)malloc(sizeof(node));

    newnode->data = data;

    // 1) insert address of head to newnode->pointer
    newnode->pointer = head;

    // 2) restate head to newnode
    head = newnode;
}

// deletion from end
// deletion from head
// display function
void display()
{
    // Starting from the first end of the code
    node *i = head;

    while (i != NULL) // if I is not null then only run while loop
    {
        printf("%d\n", i->data);

        // pointing to the next node
        // The next node address is already stored in i->pointer. we will use that only.
        i = i->pointer;
    }
    // ippud ayipothadhi just small logic anthey
}
// search function
void search(int key)
{
    // Starting from the first end of the code
    node *i = head;

    while (i != NULL) // if I is not null then only run while loop
    {
        if(key == i->data)
        {
            printf("Found");
            break;
        }
        // pointing to the next node
        // The next node address is already stored in i->pointer. we will use that only.
        i = i->pointer;
    }
    // idhi kuuda
    // same logic of display but with small change
}

void randomdelete(int index)
{
    struct Node *t = head;

    int i = 0;

    while((i < index - 1) && (t != NULL))
    {
        // going to next node -> just like i++ in for loop 
        t = t->pointer;
        i ++;
    }

    struct Node *temp;

    temp = t->pointer; // temp will point to 2
    t->pointer = temp->pointer; // storing 3's address in 1's pointer
    free(temp); // deleting temp

}

void randominsert(int data, int index)
{
    // create memory for the data
    struct Node *t = (struct Node*) malloc(sizeof(struct Node));

    // insert data into the node
    t->data = data;

    // NULL value to node
    t->pointer = NULL;

    // This points to the first node in the linked list
    struct Node *temp = head;

    // This is same as i in for loop
    int i = 0;

    while((i < index - 1) && (temp != NULL))
    {
        // going to next node -> just like i++ in for loop 
        temp = temp->pointer;
        i ++;
    }

    
    t->pointer = temp->pointer; // 1) 
    temp->pointer = t; // 2)
}

void main()
{
    for (int i = 1; i <= 3; i++)
    {
        insertfromend(i);
    }
    insertfromfront(100);
    display();
    search(3);
}