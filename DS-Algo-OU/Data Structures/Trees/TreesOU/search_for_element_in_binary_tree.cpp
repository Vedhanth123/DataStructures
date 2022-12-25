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

    root->left->left = new struct BT;
    root->left->left->data = 5;

    root->left->left->right = new struct BT;
    root->left->left->right->data = 12;

}

int search(struct BT *t, int data)
{
    if(!t)
    {
        return NULL;
    }
    
    if(t->data == data)
    {
        return data;
    }
    else if(data < t->data)
    {
        return search(t->left, data);
    }
    else
    {
        return search(t->right, data);
    }
}
int main()
{
    construct_a_binary_tree();
    cout << search(root, 12);
    cout << "\n";
    cout << search(root, 56);

}