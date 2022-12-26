#include <iostream>
using namespace std;

struct BT
{
    int data;
    struct BT *left, *right;
};


// function to allocate memory
struct BT* getNode(int data)
{
    struct BT* newnode = new struct BT;

    newnode->data = data;
    newnode->left = NULL;
    newnode->right = NULL;

}

struct BT *root = NULL;

struct BT* insert(struct BT *t, int data, struct BT* newnode)
{
    if(!newnode)
    {
        newnode = getNode(data);
    }
    if(!root)
    {
        root = newnode;
    }
    if(!t)
    {
        return newnode;
    }
    else if(data <= t->data)
    {
        t->left = insert(t->left, data, newnode);
    }
    else
    {
        t->right = insert(t->right, data, newnode);
    }
    return t;
}

int main()
{
    int i = 100;
    while(i > 0)
    {
      insert(root, i, NULL);
      i -= 25;
    }
    i = 100;
    while(i < 200)
    {
      i += 25;
      insert(root, i, NULL);
    }
    
}