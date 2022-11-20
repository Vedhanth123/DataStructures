/*
*/

#include <iostream>
#include <string>
using namespace std;

// create a class of Stack and write down all the functions of the stack in it
template <typename T>
class Stack
{
    T Stack[10];
    int sp = 0;

public:
    void push(T a);
    void pop();
};

template <typename T>
void Stack<T>::push(T a)
{
    // check for overflow condition
    if (sp >= 10)
    {
        cout << "Stack in overflow condition";
    }
    else
    {
        Stack[sp] = a;
        sp += 1;
    }
}

template <typename T>
void Stack<T>::pop()
{
    if (sp < 0)
    {
        cout << "Stack in underflow condition";
    }
    else
    {
        sp -= 1;
        cout << Stack[sp];
        Stack[sp] = NULL;
    }
}
int main()
{
    // create a stack object

    Stack<int> s1;
    for (int i = 0; i <= 11; i++)
    {
        s1.push(i * 10);
    }
    for (int i = 0; i <= 11; i++)
    {
        s1.pop();
    }
    return 0;
}