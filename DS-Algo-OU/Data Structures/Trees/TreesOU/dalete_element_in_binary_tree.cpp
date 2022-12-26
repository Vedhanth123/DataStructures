#include <iostream>
using namespace std;

struct BT
{
    int data;
    struct BT *left, *right;
};


// function to allocate memory
struct BT* getNode(int data)
{
    struct BT* newnode = new struct BT;

    newnode->data = data;
    newnode->left = NULL;
    newnode->right = NULL;

}

struct BT *root = NULL;

// function to find out the smallest element in the tree
struct BT* smallest_element(struct BT *t)
{
    if(!t)
    {
        return NULL;
    }
    if(!t->left)
    {
        return t;
    }
    else
    {
        return smallest_element(t->left);
    }
}


struct BT* largest_element(struct BT *t)
{
    if(!t)
    {
        return NULL;
    }
    if(!t->right)
    {
        return t;
    }
    else
    {
        return largest_element(t->right);
    }
}

// we have 3 test cases 

// case 1: node has no children
// case 2: node has only 1 children
// case 3: node has 2 children

// case 1:
struct BT* delete_child(struct BT* t, int data)
{
    if(!t)
    {   
        return 0;
    }
    // search for the element in the tree
    if(data == t->data)
    {
        // case 1
        if(!t->left && !t->left)
        {
            cout << "Deleting Element: " << t->data << endl;
            free(t);
        }
        // case 2: if the the node has only one child
        // node has right child but not left child
        else if(!t->left && t->right)
        {
            struct BT *newnode = NULL;
            cout << "Deleting Element: " << t->data << endl;
            newnode = new struct BT;
            newnode = t->right;
            free(t);
            return newnode;
        }
        // node has left child but not right child
        else if(t->left && !t->right)
        {
            struct BT *newnode = NULL;
            cout << "Deleting Element: " << t->data << endl;
            newnode = new struct BT;
            newnode = t->left;
            free(t);
            return newnode;
        }
        // case 3: if the node has both the children
        else
        {
            // 1) Search for the element in the tree
            // 2) Move right
            struct BT *right = t->right;

            // 3) Find the smallest element in the right subtree
            struct BT *s1 = smallest_element(right);

            // 4) insert the left child of the node [which is to be deleted] to the smallest element's left pointer in the right subtree.
            s1->left = t->left;

            // 4) find the largest element in the s1 subtree and name it le
            struct BT *le = largest_element(s1);

            // 5) insert the right child of the node [which is to be deleted] to the le's right pointer
            le->right = t->right;

            // 6) delete the node
            
            // 7) printing the node to be deleted.
            free(t);

            return s1;
        }
    }
    if(data <= t->data)
    {
        t->left = delete_child(t->left, data);
    }
    else if(data > t->data)
    {
        t->right = delete_child(t->right, data);
    }

}

int main()
{
    
    root = new BT;
    root->data = 100;

    root->left = new BT;
    root->left->data = 75;

    root->right = new BT;
    root->right->data = 125;

    root->left->left = new BT;
    root->left->left->data = 60;
    root->left->right->data = 80;

    root->right->left = new BT;
    root->right->left->data = 115;
    root->right->right->data = 130;

    delete_child(root, 130);
    delete_child(root, 125);
    delete_child(root, 75);

}