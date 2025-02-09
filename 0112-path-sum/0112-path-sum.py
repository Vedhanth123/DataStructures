# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        if(root):
            def dfs(root, target, total):
            
                if(root):

                    if(not root.left and not root.right):
                        if(target == total+root.val):
                            return True
                        else:
                            return False

                    return dfs(root.left, target, total+root.val) or dfs(root.right,target, total+root.val)
                else:
                    return False
                    
            return dfs(root, targetSum, 0)
        
        return False