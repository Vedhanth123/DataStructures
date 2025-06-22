# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0
        def helper(root):

            if(root):
                left_depth = helper(root.left)
                right_depth = helper(root.right)
                self.diameter = max(self.diameter, left_depth + right_depth)
                return max(left_depth,right_depth) + 1
            else:
                return 0
        
        helper(root)
        return self.diameter
            