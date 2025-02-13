# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def find_min(root):
            
            while(root and root.left):
                root = root.left
            return root

        def delete(root,key):

            if(root):

                if(key == root.val):

                    if(not root.left and not root.right):
                        return None
                    elif(not root.left and root.right):
                        return root.right
                    elif(root.left and not root.right):
                        return root.left
                    else:

                        mini = find_min(root.right)
                        mini.right = delete(root.right, mini.val)
                        mini.left = root.left
                        return mini
                else:
                    if(key < root.val):
                        root.left = delete(root.left,key)
                    if(key > root.val):
                        root.right = delete(root.right,key)
                
            return root

        return delete(root,key)