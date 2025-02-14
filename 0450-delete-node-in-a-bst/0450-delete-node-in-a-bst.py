# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # delete a node in the binary search tree

        def find_min(root):
            while(root and root.left):
                root = root.left
            return root
    
        def delete(root,val):

            if(root):

                if(val == root.val):

                    if(not root.left and not root.right):
                        return None
                    elif(root.left and not root.right):
                        return root.left
                    elif(not root.left and root.right):
                        return root.right
                    else:
                        small = find_min(root.right)
                        small.right = delete(root.right,small.val)
                        small.left = root.left
                        return small
                else:

                    if(val < root.val):
                        root.left = delete(root.left, val)
                    else:
                        root.right = delete(root.right,val)
            return root
        
        return delete(root,key)