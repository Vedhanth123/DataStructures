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
    // checking if the memory is allocated for the node
    if(!newnode)
    {
        newnode = getNode(data);
    }
    // checking if the root is empty
    if(!root)
    {
        root = newnode;
    }
    // checking if the t is empty
    if(!t)
    {
        return newnode;
    }
    // checking if the data is less than the root of the subtree
    else if(data <= t->data)
    {
        // traversing to left subtree
        t->left = insert(t->left, data, newnode);
    }
    // checking if the data is greater than the root of the subtree
    else
    {
        // traversing to the right subtree
        t->right = insert(t->right, data, newnode);
    }
    // returning the node
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