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
  if(temp->left != NULL)
    search_smallest(temp->left);
  else
    return temp;
}
node *search_largest(node *temp)
{
  if(temp->right != NULL)
    search_largest(temp->right);
  else
    return temp;
}

node *check(node *temp){
  if(!temp->l && temp->r == NULL)
     return temp->l;
  if(temp->l == NULL && !temp->r)
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
            if(temp->l != NULL && temp->r == NULL)
            {
                node *t = temp->l;
                free(temp);
                return t;
            }
            // code to delete 1 right child
            if(temp->l == NULL && temp->r != NULL)
            {
                node *t = temp->r;
                free(temp);
                return t;
            }
            // code to delete 2 children
            // 
            if(temp->left != NULL && temp->right != NULL)
            {
              // 1) move to right
              node *move_right = temp->right;
              // 2) find the smallest element in the right subtree
              node *smallest_element = search_smallest(move_right);
              // 3) 
        }
    }
}
node *inorder(node *temp)
{
    if (temp)
    {
        inorder(temp->l);
        printf("%d\t", temp->data);
        inorder(temp->r);
    }
}
int main()
{
    root = insert(root, 10);
    insert(root, 12);
    insert(root, 8);
    insert(root, 15);
    del(root, 8);
    del(root,12);
    inorder(root);
}