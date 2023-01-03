#include <stdio.h>
#include <stdlib.h>
typedef struct node
{
    struct node *l;
    int data;
    struct node *r;
} node;
node *root = NULL;
node *getnode()
{
    node *temp = (node *)malloc(sizeof(node));
    return temp;
}
node *create(int data)
{
    node *temp = getnode();
    temp->data = data;
    temp->l = temp->r = NULL;
    return temp;
}

node *insert(node *temp, int data)
{
    if (temp == NULL)
        return create(data);
    if (data <= root->data)
        temp->l = insert(temp->l, data);
    else if (data >= root->data)
        temp->r = insert(temp->r, data);
    return temp;
}
node *search(node *temp, int data)
{
    if (data <= temp->data)
        search(temp->l, data);
    else
        search(temp->r, data);
}
node *search_smallest(node *temp)
{
    if (temp->l != NULL)
        search_smallest(temp->l);
    else
        return temp;
}
node *search_largest(node *temp)
{
    if (temp->r != NULL)
        search_largest(temp->r);
    else
        return temp;
}

node *parent_of_smallest_element(int smallest, node *temp) {

    if(temp->l->data == smallest)
        return temp;
    if(smallest < temp->data)
        return parent_of_smallest_element(smallest, temp->l);
    if(smallest > temp->data)
        return parent_of_smallest_element(smallest, temp->r);
}

node *check(node *temp)
{
    if (!temp->l && temp->r == NULL)
        return temp->l;
    if (temp->l == NULL && !temp->r)
        return temp->r;
}
node *del(node *root, int data)
{
    if (root == NULL)
        return root;
    else
    {
        if (data < root->data)
            root->l = del(root->l, data);
        else if (data > root->data)
            root->r = del(root->r, data);
        else
        {
            node *temp = root;
            // code to delete 0 children
            if (root->l == NULL && root->r == NULL)
            {
                free(temp);
                return NULL;
            }
            // code to delete 1 left child
            if (temp->l != NULL && temp->r == NULL)
            {
                node *t = temp->l;
                free(temp);
                return t;
            }
            // code to delete 1 right child
            if (temp->l == NULL && temp->r != NULL)
            {
                node *t = temp->r;
                free(temp);
                return t;
            }
            // code to delete 2 children
            //
            if (temp->l != NULL && temp->r != NULL)
            {
                // 1) move to right
                node *mr = temp->r;
                // 2) find the smallest element in the right subtree
                node *sn = search_smallest(mr);
                // 3) right child of the smallest will move to its parent's left pointer
                node *smallest_parent = parent_of_smallest_element(sn->data, root);
                smallest_parent->l = sn->r;
                // 4) right child of the deleted node will be added to right child of the smallest node
                sn->r = temp->r;
                // 5) the left child of the deleted node will be added to the left child of the smallest node
                sn->l = temp->l;
                free(temp);
                return sn;
            }
        }
    }
}
node *inorder(node *temp)
{
    if (temp)
    {
        printf("%d\t", temp->data);
        inorder(temp->l);
        inorder(temp->r);
    }
}
int main()
{
    root = insert(root, 60);
    insert(root, 70);
    insert(root, 10);
    insert(root, 5);
    insert(root, 50);
    insert(root, 40);
    insert(root, 15);
    insert(root, 25);
    insert(root, 20);
    insert(root, 30);
    insert(root, 55);
    inorder(root);
    del(root, 10);
    inorder(root);
}