#include <stdio.h>
// #include <conio.h>

// Let's create a struct with
// 1) data
// 2) pointer
// 3) index variables inside it.

struct LinkedList
{
    int data;
    struct LinkedList *pointer;
};

// Create a pointer which points to the head of the node
struct LinkedList *head = NULL;
struct LinkedList *node;

void CreateNewNode(int data)
{

    node = (struct LinkedList *)malloc(sizeof(struct LinkedList));
    if (head == NULL)
    {
        head = node;
    }
}

int main()
{
    // write a function to create a new Node

    CreateNewNode(10);
}