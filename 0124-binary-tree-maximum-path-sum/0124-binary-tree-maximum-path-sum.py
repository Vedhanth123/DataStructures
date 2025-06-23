# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_sum = float("-inf")

        def dfs(root):

            if(root):
                left_gain = dfs(root.left)
                right_gain = dfs(root.right)
                sum_ = root.val + max(left_gain, right_gain)
                self.max_sum = max(self.max_sum,root.val + left_gain + right_gain, root.val + left_gain, root.val + right_gain,root.val)
                return sum_
            else:
                return 0
        
        dfs(root)
        return self.max_sum