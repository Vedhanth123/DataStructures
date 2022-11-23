#include <iostream>
using namespace std;

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

// Traversing Trees in preorder
void preorder(struct node *tree)
{
    if (tree != NULL)
    {
        cout << tree->data;
        preorder(tree->left);
        preorder(tree->right);
    }
}

// Traversing Trees in inorder
void inorder(struct node *tree)
{
    if (tree != NULL)
    {
        inorder(tree->left);
        cout << tree->data;
        inorder(tree->right);
    }
}

// Traversing Trees in postorder
void postorder(struct node *tree)
{
    if (tree != NULL)
    {
        postorder(tree->left);
        postorder(tree->right);
        cout << tree->data;
    }
}

int main()
{
    // creating a basic tree
    //      1
    // 2        3
    struct node *root = new node(1);
    root->left = new node(2);
    root->right = new node(3);

    // adding another level to tree
    //         1
    //     2       3
    // 4       5 6      7
    root->left->left = new node(4);
    root->left->right = new node(5);
    root->right->left = new node(6);
    root->right->right = new node(7);

    cout << "Preorder: ";
    preorder(root);
    cout << "\n";

    cout << "Inorder: ";
    inorder(root);
    cout << "\n";

    cout << "Postorder: ";
    postorder(root);
    cout << "\n";
    
    
}