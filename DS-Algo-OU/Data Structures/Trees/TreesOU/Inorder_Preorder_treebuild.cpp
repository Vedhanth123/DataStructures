#include <iostream>
#include <string>
using namespace std;

// create a structure to store tree data members
struct BTnode
{
    int data;
    struct BTnode *left;
    struct BTnode *right;
} *head = NULL;

// storing preorder and inorder elements into the arrays
int preorder[] = {3, 9, 20, 15, 7};
int inorder[] = {9, 3, 15, 20, 7};
int preorder_index = 0;

// creating function to build tree
struct BTnode *buildTree(int preorder[], int inorder[], int left_inroder, int right_inorder)
{
    if(preorder_index == 5)
    {
        return NULL;
    }
    if (left_inroder >= right_inorder)
    {
        return NULL;
    }

    // create a node

    struct BTnode *node = (struct BTnode *)malloc(sizeof(struct BTnode));
    if (head == NULL)
    {
        head = node;
    }

    // insert data into the node
    node->left = NULL;
    node->right = NULL;
    node->data = preorder[preorder_index];
    preorder_index += 1;

    // search for the element in the inorder
    int element_found_at = 0;
    for (int i = left_inroder; i < right_inorder; i++)
    {
        if (inorder[i] == node->data)
        {
            element_found_at = i;
            break;
        }
    }

    // look for the left elements in inorder and build left subtree
    node->left = buildTree(preorder, inorder, left_inroder, element_found_at - 1);
    node->right = buildTree(preorder, inorder, element_found_at + 1, right_inorder);

    return node;
}

void preorder_traversal(struct BTnode *head)
{
    if (head != NULL)
    {
        cout << head->data << endl;
        preorder_traversal(head->left);
        preorder_traversal(head->right);
    }
}

int main()
{
    struct BTnode *firstnode = buildTree(preorder, inorder, 0, 5);
    preorder_traversal(firstnode);
    return 0;
}