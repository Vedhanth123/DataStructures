# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root):
        memo = {}
        def helper(root):

            if(not root):
                return 0
            if(root in memo):
                return memo[root]

            not_rob = helper(root.left) + helper(root.right)

            rob = root.val
            if(root.left):
                rob += helper(root.left.left) + helper(root.left.right)
            if(root.right):
                rob += helper(root.right.right) + helper(root.right.left)

            memo[root] = max(not_rob, rob)
            return memo[root]
        
        return helper(root)
