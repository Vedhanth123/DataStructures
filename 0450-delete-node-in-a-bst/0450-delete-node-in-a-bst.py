# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def smallestVal(self, root):

        while(root.left):
            root = root.left
        else:
            return root
    
    def largestVal(self,root):
        if(root.right):
            return self.largestVal(root.right)
        else:
            return root


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if(root):

            if(root.val == key):
                if(not root.left and not root.right):
                    return None
                elif(not root.left and root.right):
                    return root.right
                elif(root.left and not root.right):
                    return root.left
                else:
                    smallest = self.smallestVal(root.right)
                    smallest.right = self.deleteNode(root.right, smallest.val)
                    smallest.left = root.left
                    return smallest
            
            else:
                if(key < root.val):
                    root.left = self.deleteNode(root.left,key)
                else:
                    root.right = self.deleteNode(root.right,key)
            return root
