#include<stdio.h>
#include <stdlib.h>


// We use structure to create nodes

// why union is not used instead of structure in linked list?
// Ans: Union cannot store two values at a time. That is why union is not used

// instead of structure what else can be used?
// Ans: classes which are used in java, c++, python

// Java doesn't have pointers right, How do you link nodes with each other?
// Ans: reference

// What are the advantages and disadvantages of LinkedList when compared to array
// Ans: Advantages: dynamic linking, Disadvantages: searching is very slow, or traversing is very slow O(n)

// To solve this issue what data structure do we use?
// Ans: Hashmaps. 

// Heap, Tree, Graph -> Non Linear
// Hashmap, Array, Stack, Queue -> Linear



struct Node
{
    int data;
    struct Node *pointer;
};

struct Node *head = NULL, *newnode = NULL, *linker = NULL;


void insert(int data)
{
    // allocate memory
    newnode = (struct Node*) malloc(sizeof(struct Node*));

    // inserting data into node
    newnode->data = data; // machine code : *(newnode).data;

    // NULL value to pointer so that we don't get error in our code
    newnode->pointer = NULL; // machine code

    if(head != NULL)
    {
        head = newnode;
    }
    else
    {
        // link old nodes to new nodes
        linker->pointer = newnode;
    }

    // updating the linker
    linker = newnode;
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
void main()
{
    for(int i = 1; i <= 4 ;i ++)
    {
        insert(i*10);
    }

    randominsert(100, 2);

    randomdelete(3);
}