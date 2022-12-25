#include <iostream>
using namespace std;

struct BT
{
    int data;
    struct BT *left;
    struct BT *right;
};

struct BT *root;

int Binary_Tree_Height(struct BT *t)
{
    if(!t)
    {
        return 0;
    }
    else
    {
        int left_height = Binary_Tree_Height(t->left);
        int right_height = Binary_Tree_Height(t->right);

        if(left_height > right_height) 
            return left_height + 1;
        else
            return right_height + 1;
    }
}
int main()
{
    root = (struct BT*) malloc(sizeof(struct BT));
    root->left = (struct BT*) malloc(sizeof(struct BT));
    root->left->left = (struct BT*) malloc(sizeof(struct BT));
    root->left->left->left = (struct BT*) malloc(sizeof(struct BT));

    cout << Binary_Tree_Height(root);
}
