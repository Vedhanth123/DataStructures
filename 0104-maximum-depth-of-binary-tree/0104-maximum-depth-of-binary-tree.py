# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        


        def height(root):
            
            if(root):
                return max(height(root.left), height(root.right)) + 1
            else:
                return 0


        return height(root)
        

