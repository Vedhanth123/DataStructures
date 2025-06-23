# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSameTree(self, s, t):

        if(not s and not t):
            return True
        
        if(not s or not t or s.val != t.val):
            return False
        
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if(not root):
            return False
        
        if(self.isSameTree(root, subRoot)):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)

    