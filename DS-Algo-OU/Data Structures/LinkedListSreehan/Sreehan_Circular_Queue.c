#include <stdio.h>

int Queue[5];

int insert = 0;
int delete1 = -1;

void enque(int data)
{
    if (insert == delete1)
    {
        printf("Queue is full:\n");
    }
    else
    {
        if (insert == 5)
        {
            insert = 0;
        }
        Queue[insert] = data;
        insert++;
    }
}

void deque()
{

    delete1++;
    if (delete1 == insert)
    {
        printf("Queue is empty:\n");
    }
    else
    {
        if (delete1 == 5)
        {
            delete1 = 0;
        }
        Queue[delete1] = 0;
    }
}

int main()
{
    for (int i = 1; i < 4; i++)
    {
        enque(i * 10);
    }
    for (int i = 1; i < 5; i++)
    {
        deque();
    }
    for (int i = 1; i < 7; i++)
    {
        enque(i * 10);
    }
}