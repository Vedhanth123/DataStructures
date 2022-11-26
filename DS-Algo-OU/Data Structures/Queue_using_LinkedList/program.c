#include <stdio.h>

struct Queue
{
    int data;
    struct Queue *pointer;
};

typedef struct Queue Queue;

// create two pointers which take care of enque and deque operations
Queue *enque = NULL;
Queue *deque = NULL;

void Enque(int data)
{
    // create a node and store data into that node
    Queue *node = (Queue *) malloc(sizeof(Queue));

    node->data = data;
    node->pointer = NULL;

    if(deque == NULL)
    {
        deque = node;
    }
    else{
        enque->pointer= node;
    }
    enque = node;
}

void Deque()
{
    // check for underflow condition
    if(deque == NULL)
    {
        printf("Queue is empty");
    }
    else
    {
        Queue *temp = deque;
        deque = deque->pointer;
        free(temp);
    }
}

void main()
{
    for(int i = 0; i < 5; i++)
    {
        Enque(i*10);
    }
    for(int i= 0; i < 6; i ++)
    {
        Deque();
    }
}