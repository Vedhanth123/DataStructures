#include <stdio.h>
#include <stdlib.h>

// Stack using array --------------------------------------------
int stack[5], i, j, option = 0, n = 5, topstack = -1;
// Push operation function
void push(int val)
{
    if (topstack == n)
        printf("\n Overflow\n");
    else
    {
        topstack = topstack + 1;
        stack[topstack] = val;
    }
}

// Pop operation function
void pop()
{
    if (topstack == -1)
        printf("\n Underflow\n");
    else
    {
        printf("%d ", stack[topstack]);
        topstack = topstack - 1;
    }
}

// Queue using array ---------------------------------------------------------
int ar[5];
int frontqueue = -1;
int rearqueue = -1;

void enqueue(int item)
{
    if (rearqueue == n - 1)
    {
        printf("\nOverflow\n");
    }
    else
    {
        if (frontqueue == -1 && rearqueue == -1)
        {
            frontqueue = 0;
            rearqueue = 0;
        }
        else
        {
            rearqueue++;
        }
        ar[rearqueue] = item;
    }
}
void dequeue()
{

    if (frontqueue == -1 || frontqueue > rearqueue)
    {
        printf("\nUnderflow\n");
    }
    else
    {
        printf("%d Element deleted: ", ar[frontqueue]);
        if (frontqueue == rearqueue)
        {
            frontqueue = -1;
            rearqueue = -1;
        }
        else
        {
            frontqueue++;
        }
    }
}

// Stack using Linked List -------------------------------------------------------
// Structure to create a node with data and the next pointer
struct node
{
    int data;
    struct node *next;
};
struct node *top = NULL;

// Push() operation on a  stack
void pushlinkedlist(int value)
{
    struct node *newnode;
    newnode = (struct node *)malloc(sizeof(struct node));
    newnode->data = value; // assign value to the node
    if (top == NULL)
    {
        newnode->next = NULL;
    }
    else
    {
        newnode->next = top; // Make the node as top
    }
    top = newnode; // top always points to the newly created node
    printf("node is Inserted\n\n");
}

int poplinkedlist()
{
    if (top == NULL)
    {
        printf("\nStack Underflow\n");
    }
    else
    {
        struct node *temp = top;
        int temp_data = top->data;
        top = top->next;
        free(temp);
        return temp_data;
    }
}

// Queue using Linked List --------------------------------------------------
struct node *front = NULL;
struct node *rear = NULL;
struct node *ptr;

// Enqueue() operation on a queue
void enqueuelinkedlist(int value)
{
    struct node *ptr;
    ptr = (struct node *)malloc(sizeof(struct node));
    ptr->data = value;
    ptr->next = NULL;
    if ((front == NULL) && (rear == NULL))
    {
        front = rear = ptr;
    }
    else
    {
        rear->next = ptr;
        rear = ptr;
    }
    printf("node is Inserted\n\n");
}

// Dequeue() operation on a queue
int dequeuelinkedlist()
{
    if (front == NULL)
    {
        printf("\nUnderflow\n");
        return -1;
    }
    else
    {
        struct node *temp = front;
        int temp_data = front->data;
        front = front->next;
        free(temp);
        return temp_data;
    }
}
// Taking stack array of size 50
void main()
{
    printf("Stack using array-----------------------------------\n");
    for (int i = 1; i <= 7; i++)
    {
        push(i * 10);
    }
    for (int i = 1; i <= 7; i++)
    {
        pop();
    }

    printf("Queue using array---------------------------------\n");
    for (int i = 1; i <= 7; i++)
    {
        enqueue(i * 10);
    }
    for (int i = 1; i <= 7; i++)
    {
        dequeue();
    }

    printf("Stack using Linked List -----------------------------\n");
    for (int i = 1; i <= 7; i++)
    {
        pushlinkedlist(i * 10);
    }
    for (int i = 1; i <= 7; i++)
    {
        printf("Element deleted is %d\n",poplinkedlist());
    }

    printf("Queue using Linked List ------------------------------\n");
    for (int i = 1; i <= 7; i++)
    {
        enqueuelinkedlist(i * 10);
    }
    for (int i = 1; i <= 7; i++)
    {
        printf("Element deleted is %d\n",dequeuelinkedlist());
    }
}
