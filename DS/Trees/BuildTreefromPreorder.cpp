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

node* buildTree(int preorder[], int inorder[], int start, int end)
{
    // point to elements of the preorder array
    static int idx = 0;

    // check if the inorder array is empty
    if(start > end)
    {
        // if empty return NULL
        return NULL;
    }

    // Creating a node after pointing to the element in preorder array
    node *n1 = new node(preorder[idx]);

    // incrementing index
    idx++;


    if(start == end)
    {
        return n1;
    }

    // getting the position of the element in inorder array
    int pos = search(inorder, start, end, preorder[idx]);

    // Splitting the inorder array into two parts, buildTree for left and buildTree for right
    n1->left = buildTree(preorder, inorder, start, pos - 1);
    n1->right = buildTree(preorder, inorder, pos + 1, end);

    // return the node
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