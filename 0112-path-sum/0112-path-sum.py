# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def rec(root, targetSum, total):

            if(root):
                
                if(root.left == None and root.right == None):
                    if(targetSum == total+root.val):
                        return True
                    else:
                        return False
                
                if(rec(root.left, targetSum, total+root.val) == True):
                    return True
                if(rec(root.right,targetSum, total+root.val) == True):
                    return True

                return False
            else:
                return False
        
        return rec(root, targetSum, 0)