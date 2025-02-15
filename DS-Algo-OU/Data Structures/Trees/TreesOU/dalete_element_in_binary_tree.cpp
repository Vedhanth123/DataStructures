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
int search(struct BT *t, int data)
{
    if(!t)
    {
        return 0;
    }
    
    if(t->data == data)
    {
        return data;
    }
    else if(data < t->data)
    {
        return search(t->left, data);
    }
    else
    {
        return search(t->right, data);
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


struct BT *delete_child(struct BT *root, int val)
{
    /*
     * If the node becomes NULL, it will return NULL
     * Two possible ways which can trigger this case
     * 1. If we send the empty tree. i.e root == NULL
     * 2. If the given node is not present in the tree.
     */
    if(root == NULL)
        return NULL;
    /*
     * If root->key < val. val must be present in the right subtree
     * So, call the above remove function with root->right
     */
    if(root->data < val)
        root->right = delete_child(root->right,val);
    /*
     * if root->key > val. val must be present in the left subtree
     * So, call the above function with root->left
     */
    else if(root->data > val)
        root->left = delete_child(root->left,val);
    /*
     * This part will be executed only if the root->key == val
     * The actual removal starts from here
     */
    else
    {
        /*
         * Case 1: Leaf node. Both left and right reference is NULL
         * replace the node with NULL by returning NULL to the calling pointer.
         * free the node
         */
        if(root->left == NULL && root->right == NULL)
        {
            free(root);
            return NULL;
        }
        /*
         * Case 2: Node has right child.
         * replace the root node with root->right and free the right node
         */
        else if(root->left == NULL)
        {
            struct BT *temp = root->right;
            free(root);
            return temp;
        }
        /*
         * Case 3: Node has left child.
         * replace the node with root->left and free the left node
         */
        else if(root->right == NULL)
        {
            struct BT *temp = root->left;
            free(root);
            return temp;
        }
        /*
         * Case 4: Node has both left and right children.
         * Find the min value in the right subtree
         * replace node value with min.
         * And again call the remove function to delete the node which has the min value.
         * Since we find the min value from the right subtree call the remove function with root->right.
         */
        else
        {
            int rightMin = smallest_element(root->right)->data;
            root->data = rightMin;
            root->right = delete_child(root->right,rightMin);
        }

    }

    //return the actual root's address
    return root;
}
struct BT* insert(struct BT *t, int data, struct BT* newnode)
{
    // if node is not created
    if(!newnode)
    {
        newnode = getNode(data);
    }
    // if the 
    if(!t)
    {
        t = newnode;
    }
    else if(data <= t->data)
    {
        return insert(t->left, data, newnode);

    }
    else
    {
        return insert(t->right, data, newnode);
    }

}

int main()
{
    struct BT *root = NULL;
    root = insert(root, 60, NULL);
    root = insert(root, 10, NULL);
    root = insert(root, 50, NULL);
    root = insert(root, 15, NULL);
    root = insert(root, 70, NULL);
    root = insert(root, 75, NULL);
    root = insert(root, 85, NULL);
    root = insert(root, 30, NULL);
    root = insert(root, 40, NULL);
    
    cout << "smallest element " << smallest_element(root)->data << "\n";
    cout << "largest element " << largest_element(root)->data << "\n";
    cout << "element " << search(root, 60) << "\n";
    delete_child(root, 60);
    delete_child(root, 15);
    delete_child(root, 70);

    return 1;
}