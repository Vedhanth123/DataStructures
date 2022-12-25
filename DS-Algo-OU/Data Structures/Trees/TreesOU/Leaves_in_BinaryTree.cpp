#include <iostream>
using namespace std;

struct BT
{
    int data;
    struct BT *left;
    struct BT *right;
};

struct BT *root;

int Leaves_in_BinaryTree(struct BT *t)
{
    if(t == NULL)
    {
        return 0;
    }
    
    if(t->left == NULL && t->right == NULL)
    {
        return 1;
    }
    else
    {
        return Leaves_in_BinaryTree(t->left) + Leaves_in_BinaryTree(t->right);
    }
}

int main()
{
    root = new struct BT;
    root->left = new struct BT;
    root->left->right = new struct BT;
    root->left->right->right = new struct BT;
    root->left->left = new struct BT;

    cout << Leaves_in_BinaryTree(root);
}