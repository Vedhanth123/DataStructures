#include <iostream>
using namespace std;

// given two arrays build trees for preoder and inorder

// Algo: 
// 1) Pick element from preorder and create a node
// 2) Increment preorder idx
// 3) Search for picked elements pos in inorder
// 4) Call to build left subtree from inorder's 0 to pos 01
// 5) Call to build right subtree from inorder pos + 1 to n
// 6) Return the node

int preorder [] = {1,2,4,5,3,6,7};
int inorder [] = {4,2,5,1,6,3,7};

// Preorder: 1245367
// Inorder: 4251637
// Postorder: 4526731


// traverse the preorder array
int PickElement(int *preorder, int index)
{   
    return preorder[index];
}

int SearchPickedElement(int *inorder, int key)
{
    for(int i = 0; i < 7; i ++)
    {
        if(key == inorder[i])
        {
            return i;
        }
    }
}

int main()
{

    // search for picked element in inorder array
    return 1;
}