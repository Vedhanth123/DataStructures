#include <stdio.h>
#include <stdlib.h>


int Queue[10];

int ins_rear = 0;
int ins_front = 9;
int del_front = -1;
int del_rear = 10;

void insert_rear(int data)
{
    // check if ins_rear anddel_front is same
    if (ins_rear == ins_front+1)
    {
        printf("Queue is full\n");
    }
    else
    {
        if (ins_rear == 10)
        {
            ins_rear = 0;
        }
        Queue[ins_rear] = data;
        ins_rear++;
    }
}

void delete_front()
{
    if (del_front > 9 || del_front+1 == del_rear)
    {
        printf("Queue is empty:\n");
    }
    else
    {
        del_front++;
        if (del_front == 10)
        {
            del_front = -1;
        }
        printf("%d", Queue[del_front]);
        Queue[del_front] = 0;
    }
}

void insert_front(int data)
{
    if (ins_rear-1 == ins_front)
    {
        printf("Queue is full\n");
    }
    else
    {
        if (ins_front == -1)
        {
            ins_front = 9;
        }
        Queue[ins_front] = data;
        ins_front--;
    }
}

void delete_rear()
{
    if (del_rear < 0 || del_rear == del_front-1)
    {
        printf("Queue is empty");
    }
    else
    {
        del_rear--;
        if (del_rear == -1)
        {
            del_rear = 10;
        }
        printf("%d", Queue[del_rear]);
        Queue[del_rear] = 0;
    }
}

int main()
{
  for(int i = 1;i <= 6; i++)
  {
    insert_front(i*10);
  }
  for(int i = 1;i <= 7; i++)
  {
    insert_rear(i*100);
  }
  for(int i = 1; i <= 6; i ++)
  {
    delete_front();
  }
  for(int i = 1; i <= 7; i++)
  {
    delete_rear();
  }
}