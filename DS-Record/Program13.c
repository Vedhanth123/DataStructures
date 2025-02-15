#include <stdio.h>
#include <stdlib.h>
 
struct node {
    int data;
    struct node *left;
    struct node *right;
};
 
struct node* getNewNode(int data) {
  struct node* newNode = (struct node*)malloc(sizeof(struct node));
  newNode->data = data;
  newNode->left = NULL;
  newNode->right = NULL;
   
  return newNode;
}
struct node* getMirrorBinaryTree(struct node *root){
    if(root == NULL)
        return NULL;
    struct node* newNode = getNewNode(root->data);
    newNode->right = getMirrorBinaryTree(root->left);
    newNode->left = getMirrorBinaryTree(root->right);
 
    /* Return root of mirrored tree */
    return newNode;
}
struct node* generateBTree(){
    struct node* root =  getNewNode(1);
  
    root->left = getNewNode(9);
    root->right = getNewNode(12);
  
    root->left->left = getNewNode(4);
    root->left->right = getNewNode(50);
    root->right->right = getNewNode(-7);
  
    root->left->left->left = getNewNode(18);
    root->left->left->right = getNewNode(9);
     
    return root;
}

struct node* cloneBinaryTree(struct node *root){
    if(root == NULL)
        return NULL;
    struct node* newNode = getNewNode(root->data);
    newNode->left = cloneBinaryTree(root->left);
    newNode->right = cloneBinaryTree(root->right);
    /* Return root of cloned tree */
    return newNode;
}

void inOrderTraversal(struct node *nodeptr){
    if(nodeptr != NULL){

        inOrderTraversal(nodeptr->left);

        printf("%d ", nodeptr->data);
 
        inOrderTraversal(nodeptr->right);
    }
}

void deleteTree(struct node *root){
    if(root == NULL)
        return;
    /* Delete Left sub-tree */
    deleteTree(root->left);
    /* Delete right sub-tree */
    deleteTree(root->right);
     
    /* At last, delete root node */
    printf("Deleteing Node : %d\n", root->data);
    free(root);
     
    return;
}

int tree_height(struct node* root) {
    // Get the height of the tree
    if (!root)
        return 0;
    else {
        // Find the height of both subtrees
        // and use the larger one
        int left_height = tree_height(root->left);
        int right_height = tree_height(root->right);
        if (left_height >= right_height)
            return left_height + 1;
        else
            return right_height + 1;
    }
}

void print_level(struct node* root, int level_no) {
    // Prints the nodes in the tree
    // having a level = level_no
    
    // We have a auxiliary root node
    // for printing the root of every
    // subtree
    if (!root)
        return;
    if (level_no == 0) {
        // We are at the top of a subtree
        // So print the auxiliary root node
        printf("%d -> ", root->data);
    }
    else {
        // Make the auxiliary root node to
        // be the left and right nodes for
        // the subtrees and decrease level by 1, since
        // you are moving from top to bottom
        print_level(root->left, level_no - 1);
        print_level(root->right, level_no - 1);
    }

}

void print_tree_level_order(struct node* root) {
    if (!root)
        return;
    int height = tree_height(root);
    for (int i=0; i<height; i++) {
        printf("Level %d: ", i);
        print_level(root, i);
        printf("\n");
    }
    printf("\n\n-----Complete Level Order Traversal:-----\n");
    for (int i=0; i<height; i++) {
        print_level(root, i);
    }
    printf("\n");
}


int main() {
    struct node *clone,*mirror,*root  = generateBTree();    
    printf("Original Tree\n");
    inOrderTraversal(root);
     
    clone = cloneBinaryTree(root);
    printf("\nClone Tree\n");
    inOrderTraversal(clone);

    printf("\nMirror Tree\n");
    mirror = getMirrorBinaryTree(root);
    inOrderTraversal(mirror);

    printf("Level Order:\n");
    print_tree_level_order(root);

    printf("\nDeleting Tree\n");
    inOrderTraversal(mirror);
    deleteTree(mirror);
    inOrderTraversal(mirror);
    return 0; 
}