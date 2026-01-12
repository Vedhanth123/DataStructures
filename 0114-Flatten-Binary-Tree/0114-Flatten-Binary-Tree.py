# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        dummy = TreeNode()
        temp = dummy

        def helper(root):

            nonlocal temp
            if(not root): 
                return None
            temp.right = TreeNode(root.val)
            temp = temp.right
            helper(root.left)
            helper(root.right)

        helper(root)
        return dummy.right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

Solution().flatten(root)