#include <iostream>
using namespace std;

// given two arrays build trees for preoder and inorder

// Algo:
// 1) Pick element from preorder and create a node
// 2) Increment preorder idx
// 3) Search for picked elements pos in inorder
// 4) Call to build left subtree from inorder's 0 to pos 01
// 5) Call to build right subtree from inorder pos + 1 to n
// 6) Return the node

int preorder[] = {1, 2, 4, 3, 5};
int inorder[] = {4, 2, 1, 5, 3};

// We have to create a structure to create a node
struct node
{
    int data;
    struct node *left;
    struct node *right;

    // constructor for structure
    node(int val)
    {
        data = val;
        left = NULL;
        right = NULL;
    }
};

typedef struct node node;

// function to check for the position of the current element
int search(int *inorder, int start, int end, int curr)
{
    for (int i = start; i <= end; i++)
    {
        if (curr == inorder[i])
        {
            return i;
        }
    }
    return -1;
}

// creating a function to display the tree
// Traversing Trees in preorder
void preorder_traversal(node *tree)
{
    if (tree != NULL)
    {
        cout << tree->data;
        preorder_traversal(tree->left);
        preorder_traversal(tree->right);
    }
}

// Traversing Trees in inorder
void inorder_traversal(node *tree)
{
    if (tree != NULL)
    {
        inorder_traversal(tree->left);
        cout << tree->data;
        inorder_traversal(tree->right);
    }
}

node *buildTree(int *preorder, int *inorder, int inorder_start, int inorder_end)
{
    // This is a variable which is used as an index for preorder and we don't want it to change everytime to new number after we recurse the function so we have used static keyword.
    static int idx = 0;

    // create node for every element in preorder array
    int curr = preorder[idx];

    // incrementing the index
    idx++;

    if (inorder_start > inorder_end)
    {
        return NULL;
    }

    node *n1 = new node(curr);
    if (inorder_start == inorder_end)
    {
        return n1;
    }

    int pos = search(inorder, inorder_start, inorder_end, curr);

    n1->left = buildTree(preorder, inorder, inorder_start, pos - 1);
    n1->right = buildTree(preorder, inorder, pos + 1, inorder_end);

    return n1;
}

int main()
{
    node *tree = buildTree(preorder, inorder, 0, 4);
    preorder_traversal(tree);
    cout << '\n';
    inorder_traversal(tree);
    return 1;
}