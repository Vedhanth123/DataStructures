# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    good = 0
    def goodNodes(self, root: TreeNode) -> int:
        
        max_val = float("-inf")

        if(root):

            def dfs(root, max_val):

                if(root):

                    if(root.val >= max_val):
                        self.good += 1
                        max_val = max(max_val, root.val)
                    
                    dfs(root.left, max_val)
                    dfs(root.right, max_val)
        
            dfs(root, max_val)
            return self.good

            
            

