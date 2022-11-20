#include <stdio.h>
#include <conio.h>

// allocating memory for Queue
int Queue[10];

// initializing headers for the queue
int rear = -1, front = -1;

// enquing elements into queue
void enque(int data)
{
    // checking if queue is full
    if(rear == 9)
    {
        printf("Queue is full:\n");
    }
    else
    {
        // incrementing rear
        rear += 1;

        // inserting data into queue
        Queue[rear] = data;

    }
}

// deleting elements from the queue
void deque()
{
    // checking if queue is empty
    if(front == rear)
    {
        printf("Queue is empty:\n");
    }
    else
    {

        // incrementing first
        front += 1;

        // printing the element in the queue and removing it
        printf("%d\n",Queue[front]);

        Queue[front] = 0; 
    }
}

void main()
{
    for(int i = 0; i < 11; i ++)
    {
        enque((i + 1) * 10);
    }

    for(int i = 0; i < 11; i++)
    {
        deque();
    }

    getch();
}
