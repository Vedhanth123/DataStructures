# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        if(nums):

            def helper(array):
                if(array):
                    root = TreeNode(max(array))

                    ind = array.index(max(array))

                    root.left = helper(array[:ind])
                    root.right = helper(array[ind+1:])
                    return root
        
            return helper(nums)

