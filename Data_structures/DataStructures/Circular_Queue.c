// NOT TO BE WRITTEN IN RECORD!!!!!!!!!!!!!!!!!!

#include <stdio.h>

// allocating memory for the queue
int Queue[10];

// assigning headers
int front = 0, rear = 0, count = 0;

// inserting elements into queue
void enqueue(int data)
{

    // checking if queue is full
    if(count == 10)
    {
        printf("queue is full:\n");
    }
    else
    {
        // increment rear
        
        // rear += 1;
        
        count += 1;

        rear += 1;

        // insert values into Queue
        Queue[rear] = data;
    }
}

// removing elements from queue
void deque()
{
  
    // checking if queue is empty
    if(count == 0)
    {
        
        printf("Queue is empty:\n");
    }
    
    else
    {
      
        // increment front
        // front += 1;

        // decrementing counter

        if(front > 9)
            front = 0;

        count -= 1;
        
        front += 1;
        
        // printing the value which is going to be removed
        printf("%d\n",Queue[front]);
        
        // removing element 
        Queue[front] = 99;
    
    }    

}

void main()
{
    for (int  i = 0; i < 11; i++)
    {
        enqueue((i+1) * 10);
        
    }
    
    for(int i = 0; i < 11; i++)
    {
      
        deque();
    }
}
