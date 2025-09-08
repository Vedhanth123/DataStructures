# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(root):

            if(root):
                root.left, root.right = root.right, root.left
                root.left = helper(root.left)
                root.right = helper(root.right)
                return root
        
        return helper(root)