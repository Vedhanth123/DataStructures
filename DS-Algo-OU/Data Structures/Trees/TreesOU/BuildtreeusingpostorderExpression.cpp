#include <iostream>
using namespace std;

char prefix_expression[] = "AB*C+";

struct BT
{
    char element;
    struct BT *left;
    struct BT *right;
};

int expression_index = 4;
struct BT* buildTree(char prefix_expression[]) 
{
    if(expression_index == '-1')
    {
        return NULL;
    }

    if(prefix_expression[expression_index] >= 'a' && prefix_expression[expression_index] <= 'z' || prefix_expression[expression_index] >= 'A' && prefix_expression[expression_index] <= 'Z')
    {
        // creating a node and returning it
        struct BT *node = new struct BT;
        node->element = prefix_expression[expression_index];
        node->left = NULL;
        node->right = NULL;
    }
    else
    {
        struct BT *node = new struct BT;
        node->element = prefix_expression[expression_index];

        expression_index -= 1;
        node->right = buildTree(prefix_expression);
        expression_index -= 1;
        node->left = buildTree(prefix_expression);

        return node;
    }
}

void inorder_traversal(struct BT *t)
{
    if(t)
    {
        inorder_traversal(t->left);
        cout << t->element;
        inorder_traversal(t->right);
    }
}

int main()
{
    struct BT *root = buildTree(prefix_expression);
    inorder_traversal(root);
}