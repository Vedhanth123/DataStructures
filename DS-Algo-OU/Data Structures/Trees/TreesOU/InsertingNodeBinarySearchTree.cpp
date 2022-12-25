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
    if(!t)
    {
        t = newnode;
    }
    else if(data <= t->data)
    {
        return insert(t->left, data, newnode);
    }
    else
    {
        return insert(t->right, data, newnode);
    }

}

int main()
{
    struct BT* root;
    root = insert(root, 100, NULL);
    
}