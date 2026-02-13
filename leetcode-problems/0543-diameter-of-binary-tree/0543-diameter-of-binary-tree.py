# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diam = 0
        def helper(root):

            if(root):
                left_height = helper(root.left)
                right_height = helper(root.right)

                self.diam = max(self.diam, left_height + right_height)
                return max(left_height, right_height) + 1
            else:
                return 0
            
        helper(root)
        return self.diam

