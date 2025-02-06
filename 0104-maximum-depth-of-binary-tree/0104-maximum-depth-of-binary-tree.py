# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        answer = 0

        def helper(root, height):

            if(root):

                left_height = helper(root.left,height)
                right_height = helper(root.right,height)

                return 1 + max(left_height, right_height)
            else:
                return 0
        
        answer = helper(root,0)
        return answer
        