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
    return newnode;
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

struct BT* delete_child(struct BT* t, int data)
{
    if(!t)
    {   
        return 0;
    }
    if(data == t->data)
    {
        if(!t->left && !t->left)
        {
            cout << "Deleting Element: " << t->data << endl;
            delete t;
        }
        else if(!t->left && t->right)
        {
            struct BT *newnode = NULL;
            cout << "Deleting Element: " << t->data << endl;
            newnode = new struct BT;
            newnode = t->right;
            delete t;
            return newnode;
        }
        // node has left child but not right child
        else if(t->left && !t->right)
        {
            struct BT *newnode = NULL;
            cout << "Deleting Element: " << t->data << endl;
            newnode = new struct BT;
            newnode = t->left;
            delete t;
            return newnode;
        }
        // case 3: if the node has both the children
        else
        {
            struct BT *right = t->right;
            struct BT *s1 = smallest_element(right);
            s1->left = t->left;
            struct BT *le = largest_element(s1);
            le->right = t->right;
            delete t;
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
struct BT* insert(struct BT *t, int data, struct BT* newnode)
{
    if(!newnode)
        newnode = getNode(data);
    if(!root)
        root = newnode;
    if(!t)
        return newnode;
    else if(data <= t->data)
        t->left = insert(t->left, data, newnode);
    else
        t->right = insert(t->right, data, newnode);
    return t;
}

int main()
{
    insert(root, 60, NULL);
    insert(root, 50, NULL);
    insert(root, 61, NULL);
    insert(root, 45, NULL);
    delete_child(root, 45);
    return 1;
}