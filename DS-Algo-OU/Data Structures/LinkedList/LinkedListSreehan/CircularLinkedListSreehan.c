
// C program for the above operation
#include <stdio.h>
#include <stdlib.h>
 
// Structure of a linked list node
struct node {
    int info;
    struct node* next;
};
 
// Pointer to last node in the list
struct node* last = NULL;
struct node* head = NULL;
 
// Function to insert a node in the
// starting of the list
void insertAtFront(int data)
{
    // Initialize a new node
    struct node* temp = (struct node*)malloc(sizeof(struct node));
    temp->info = data;

    // If the new node is the only
    // node in the list
    if (head == NULL) {
        head = temp;
        temp->next = head;
    }
 
    // Else last node contains the
    // reference of the new node and
    // new node contains the reference
    // of the previous first node
    else {
        temp->next = head;
    }
    last->next = temp;
}
 
// Function to print the list
void viewList()
{
    // If list is empty
    if (last == NULL)
        printf("\nList is empty\n");
 
    // Else print the list
    else {
        struct node* temp;
        temp = last->next;
 
        // While first node is not
        // reached again, print,
        // since the list is circular
        do {
            printf("\nData = %d", temp->info);
            temp = temp->next;
        } while (temp != last->next);
    }
    printf("\n");
}

// Function to add a new node at the
// end of the list
void addatlast(int data)
{
    // Initialize a new node
    struct node* temp = (struct node*)malloc(sizeof(struct node));
    temp->info = data;
 
    // If the new node is the
    // only node in the list
    if (head == NULL) {
        head = temp;
        temp->next = head;
    }
 
    // Else the new node will be the
    // last node and will contain
    // the reference of head node
    else {
        last->next = temp;
    }
    last = temp;
    temp->next = head;
}

// Function to insert after any
// specified element
void randominsert(int data, int index)
{
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    temp->info = data;

    int i = 0;
    struct node *traverser = head;

    while (i < index - 1 && traverser != NULL)
    {
        traverser = traverser->next;
        i++;
    }

    temp->next = traverser->next;
    traverser->next = temp;
}

// Function to delete the first
// element of the list
void deletefirst()
{
    struct node* temp = head;
 
    // If list is empty
    if (last == NULL)
        printf("\nList is empty.\n");
 
    // Else last node now contains
    // reference of the second node
    // in the list because the
    // list is circular
    else {
        head = head->next;
        last->next = head;
        free(temp);
    }
}


// Function to delete the last node
// in the list
void deletelast()
{
    struct node* temp = head;
 
    // If list is empty
    if (head == NULL)
        printf("\nList is empty.\n");
 
    temp = last->next;
 
    // Traverse the list till
    // the second last node
    while (temp->next != last)
        temp = temp->next;
 
    // Second last node now contains
    // the reference of the first
    // node in the list
    last = temp;
    last->next = head;
    free(temp);
}
void randomdelete(int index)
{
    struct node *traverser = head, *temp;
    int i = 0;

    while (i < index - 1 && traverser != NULL)
    {
        traverser = traverser->next;
        i++;
    }

    temp = traverser->next;
    traverser->next = temp->next;
    free(temp);
}
// Driver Code
void main()
{

    int i;

    addatlast(10);
    viewList();
    insertAtFront(200);
    viewList();
    randominsert(150, 1);
    viewList();
    randomdelete(1);
    viewList();
    deletefirst();
    viewList();
    deletelast();
    viewList();
}