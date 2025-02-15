#include <stdio.h>

// Implementation of Queue
// 1) Create an array
// 2) create two pointers 1) front and 2) rear
// 3) two functions 1) insert 2) delete


// 1) Create an array
int Queue[10];

// 2) create two pointers
int front = 0;
int rear = 0;
int size = 10;

// 3) two functions 1) insert 2) delete
void insert(int data)
{
    if(front == size)
    {
        printf("Queue is full!");
    }
    else
    {
        Queue[front] = data;
        front ++;
    }
}

int delete()
{
    if(rear == size)
    {
        printf("Queue is empty!");
    }
    else
    {
        Queue[rear] = 0;
        rear ++;
    }
}
int main()
{
    // for syntax:
    // for(initialization;condition;expression) => for(startingpoint;endingpoint;stepvalue)
    for(int i = 1; i < 15; i ++)
    {
        insert(i*10);
    }
    for(int i = 1; i < 15; i ++)
    {
        delete();
    }
    return 0;
}