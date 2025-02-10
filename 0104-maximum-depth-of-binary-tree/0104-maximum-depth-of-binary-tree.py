# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        answer = 0
        if(root):

            def dfs(root,height):
                if(root):
                    return 1 + max(dfs(root.left,height),dfs(root.right,height))
                else:
                    return 0

            answer = dfs(root,0)
        
        return answer