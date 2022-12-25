#include <iostream>
using namespace std;

struct BT
{
    int data;
    struct BT *left;
    struct BT *right;
};

struct BT *root;

int inorder[] = {2,1,3};
int postorder[] = {2,3,1};

int postorder_index = 2;

struct BT* buildTree(int inorder[], int postorder[], int left_inorder, int right_inorder)
{
    if(postorder_index == -1)
    {
        return NULL;
    }
    if(left_inorder > right_inorder)
    {
        return NULL;
    }

    // create a node
    struct BT *node = new struct BT;
    node->data = postorder[postorder_index];

    int found_at = 0;
    for(int i = left_inorder; i < right_inorder; i ++)
    {
        if(inorder[i] == node->data)
        {
            found_at = i;
        }
    }

    postorder_index -= 1;
    node->right = buildTree(inorder, postorder, found_at + 1, right_inorder);
    node->left = buildTree(inorder, postorder, left_inorder, found_at - 1);

    return node;
}

void inorder_traversal(struct BT *t)
{
    if(t)
    {
        inorder_traversal(t->left);
        cout << t->data;
        inorder_traversal(t->right);
    }
}

int main()
{

    struct BT *root = buildTree(inorder, postorder, 0, 3);
    inorder_traversal(root);

}