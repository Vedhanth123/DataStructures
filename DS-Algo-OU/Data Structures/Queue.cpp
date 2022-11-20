#include <iostream>

using namespace std;

// creating a class to incorporate Queue into it
template <typename T>
class Queue1
{
    // allocating memory for the queue
    T Queue[10];
    int front = 0;
    int rear = 0;

public:
    void enque(int data);
    void deque();
};

template <typename T>
void Queue1::enque(int data)
{
    if (front == rear && front < 0)
    {
        cout << "Queue is out of range";
    }
    else
    {
        Queue[front] = data;
        front += 1;
    }
}
template <typename T>
void Queue1::deque()
{
    if(rear >= 10)
    {
        cout << "Queue is out of range";
    }
    else
    {
        cout << Queue[rear];
        Queue[rear] = NULL;
        rear += 1;
    }
}

int main()
{
    class Queue1 = q;

    for (int i = 0; i < 11; i ++)
    {
        q.enque(i * 10);
    }
    for (int i = 0; i < 11; i ++)
    {
        q.deque();
    }
}
