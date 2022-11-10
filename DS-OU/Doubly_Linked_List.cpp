#include <iostream>
using namespace std;

template <typename T>
class List
{
    public:
        T data;
        class List left;
        class List right;

        List(int data)
        {
            this.data = data;
            this.left = NULL;
            this.right = NULL;
        }
};

template <typename T>
class DoublyLinkedList
{
    // create a head object which always points to first node
    class List<int> head;

    // create a old object which points to the new node created
    class List<int> old;


    // define methods
    // 1) insert
    public:
        void insert(int data);

    // 2) display
    // 3) delete
    // 4) randomdelete
    // 5) randominsert


};

template <typename T>
void DoublyLinkedList::insert(int data)
{
    class List<int> currentNode = List(data);

    if(head == NULL)
    {
        head = currentNode;
    }
    else
    {
        currentNode.left = old;
        old.right = currentNode;
    }
    old = currentNode;

};

int main()
{
    DoublyLinkedList<int> obj = DoublyLinkedList();
    for(int i = 1; i <= 5; i ++)
    {
        obj.insert(i * 100);
    }
}