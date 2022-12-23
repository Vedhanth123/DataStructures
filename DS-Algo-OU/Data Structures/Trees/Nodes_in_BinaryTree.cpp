#include <iostream>
using namespace std;

struct BT
{
    int data;
    struct BT *left;
    struct BT *right;
};

struct BT *root;

int Nodes_in_BinaryTree(struct BT *t)
{
    if(t)
    {
        return 1 + Nodes_in_BinaryTree(t->left) + Nodes_in_BinaryTree(t->right);
    }
    else
    {
        return 0;
    }
}

int main()
{
    root = new struct BT;
    root->left = new struct BT;
    root->left->right = new struct BT;
    root->left->right->right = new struct BT;
    root->left->left = new struct BT;

    cout << Nodes_in_BinaryTree(root);
}
