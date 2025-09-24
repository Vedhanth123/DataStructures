# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root) -> int:

        def helper(root):
            if(not root):
                return 0
            else:
                return 1 + max(helper(root.left), helper(root.right))
        
        return helper(root)

if __name__ == '__main__':

    tree = TreeNode(3)
    tree.left = TreeNode(9)
    # tree.right = TreeNode(20)
    # tree.right.left = TreeNode(15)
    # tree.right.right = TreeNode(7)
    # tree.right.left.left = TreeNode(20)

    obj = Solution()
    print(obj.maxDepth(tree))
