# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if(root):

            def dfs(root, num):

                if(root and not root.left and not root.right and num+root.val == targetSum):
                    return True
                if(root):
                    
                    return dfs(root.left, num+root.val) or dfs(root.right, num+root.val)
                return False
        
            return dfs(root, 0)
        
        return False