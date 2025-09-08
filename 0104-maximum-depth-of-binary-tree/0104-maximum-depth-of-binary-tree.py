# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):

            if(root):
                return max(helper(root.left), helper(root.right))
            else:
                return 1
        
        return helper(root)