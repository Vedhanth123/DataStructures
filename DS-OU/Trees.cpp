// // Cpp programt to implement trees

// class Node
// {
//     int data;
//     class Node *left;
//     class Node *right;
// };

// // Functions of Tree
// // 1) inserting
// // 2) deletion
// // 3) traversal
// // 3.3) preorder traversal -> root, left, right
// // 3.1) inorder traversal -> left, root, right
// // 3.2) postorder traversal -> left, right, root

// // ---------------------------------------------------------------------------------------------------------------------------------------
// // Inserting

// void insert(int data)
// {

// }
/*
#include <iostream>
using namespace std;

struct bintree_node
{
    bintree_node *left;
    bintree_node *right;
    int data;
};
class bst
{
    bintree_node *root;

public:
    bst()
    {
        root = NULL;
    }
    int isempty()
    {
        return (root == NULL);
    }
    void insert(int item);
    void displayBinTree();
    void printBinTree(bintree_node *);
};
void bst::insert(int item)
{
    bintree_node *p = new bintree_node;
    bintree_node *parent;
    p->data = item;
    p->left = NULL;
    p->right = NULL;
    parent = NULL;
    if (isempty())
        root = p;
    else
    {
        bintree_node *ptr;
        ptr = root;
        while (ptr != NULL)
        {
            parent = ptr;
            if (item > ptr->data)
                ptr = ptr->right;
            else
                ptr = ptr->left;
        }
        if (item < parent->data)
            parent->left = p;
        else
            parent->right = p;
    }
}
void bst::displayBinTree()
{
    printBinTree(root);
}
void bst::printBinTree(bintree_node *ptr)
{
    if (ptr != NULL)
    {
        printBinTree(ptr->left);
        cout << "  " << ptr->data << " ";
        printBinTree(ptr->right);
    }
}
int main()
{
    bst b;
    b.insert(20);
    b.insert(10);
    b.insert(5);
    b.insert(15);
    b.insert(40);
    b.insert(45);
    b.insert(30);

    cout << "Binary tree created: " << endl;
    b.displayBinTree();
}
*/

// ------------------------------------------------------------------------------------------------------------------------------------------------------
// create a struct

#include <iostream>
using namespace std;

struct node
{
    int data;
    struct node *left;
    struct node *right;
};

struct node *root;

// create a class which has all the methods of the Trees
class Tree
{
public:
    // insert function
    void insert(int data);
    // delete function
    void preorder(); // [root, left, right]
    // in order traversal [left, root, right]
    // post order traversal [left, right, root]
};

void Tree::insert(int data)
{
    // create a node and insert data into that node
    struct node *dummynode = new struct node;

    // inserting data into nodes
    dummynode->data = data;

    // make left and right pointers of the node to NULL
    dummynode->left = NULL;
    dummynode->right = NULL;

    // create a traverser which will traverse through the tree
    struct node *traverser = root;
    struct node *prev = root;

    // check if the root of the node is not NULL
    if (root == NULL)
    {
        root = dummynode;
    }
    else
    {
        while (traverser != NULL)
        {
            prev = traverser;
            if (data > traverser->data)
            {
                traverser = traverser->right;
            }
            else
            {
                traverser = traverser->left;
            }
        }
        if (data > prev->data)
        {
            prev->right = dummynode;
        }
        else
        {
            prev->left = dummynode;
        }
    }
}
void Tree::preorder()
{
    // preorder works in the principle of traversing to root, left and right

    struct node *traverser = root;
    struct node *left_traverser = root;
    struct node *right_traverser = root;
    
}

int main()
{
    Tree t1 = Tree();
    t1.insert(10);
    t1.insert(5);
    t1.insert(20);
    t1.insert(25);
    t1.insert(35);
    t1.insert(-1);
}