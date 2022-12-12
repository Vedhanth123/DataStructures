#include <iostream>
using namespace std;

template <typename T>
class CircularQueue
{
    T Queue[10];
    int front = 0;
    int rear = -1;

public:
    void enque(int data);
    void deque();
};

template <typename T>
void CircularQueue<T>::enque(int data)
{
    if (front == rear)
    {
        cout << "Queue in overflow condition";
    }
    else
    {
        if(front >= 10)
        {
            front = 0;
        }
        Queue[front] = data;
        front += 1;
    }
}
template <typename T>
void CircularQueue<T>::deque()
{
    rear += 1;
    if(rear == front)
    {
        cout << "Queue in underflow condition";
    }
    else
    {
        if(rear >= 10)
        {
            rear = 0;
        }
        cout << Queue[rear];
        Queue[rear] = NULL;
    }
}

int main()
{
  CircularQueue<int> cq;
  for(int i =0; i< 11; i ++)
  {
    cq.enque(i*10);
  }
  for (int i = 0; i < 11; i++)
  {
    cq.deque();
  }
    
}