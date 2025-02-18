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

        # first search for the val
        def delete(root, key):
            
            if(root):

                if(root.val == key):

                    if(not root.left and not root.right):
                        return None
                    elif(root.left and not root.right):
                        return root.left
                    elif(not root.left and root.right):
                        return root.right
                    else:

                        mini = find_min(root.right)
                        mini.right = delete(root.right,mini.val)
                        mini.left = root.left
                        return mini
                
                elif(key < root.val):
                    root.left = delete(root.left, key)
                else:
                    root.right = delete(root.right, key)

            return root

        return delete(root,key)