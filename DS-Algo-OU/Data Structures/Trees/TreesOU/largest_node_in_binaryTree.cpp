#include <iostream>
using namespace std;

struct BT
{
    int data;
    struct BT *left, *right;
};

struct BT *root = NULL;

void construct_a_binary_tree()
{
    root = new struct BT;
    root->data = 100;
    
    root->left = new struct BT;
    root->left->data = 10;

    root->right = new struct BT;
    root->right->data = 150;
    root->right->right = NULL;

    root->left->left = new struct BT;
    root->left->left->data = 5;
    root->left->left->right = NULL;

    root->left->left->right = new struct BT;
    root->left->left->right->data = 12;
    root->left->left->right->right = NULL;

}

int largest_element(struct BT *t)
{
    if(!t->right)
    {
        return t->data;
    }
    else
    {
        return largest_element(t->right);
    }
}

int main()
{
    construct_a_binary_tree();
    cout << largest_element(root);
}