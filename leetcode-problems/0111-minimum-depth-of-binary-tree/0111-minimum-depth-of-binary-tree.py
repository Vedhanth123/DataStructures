# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root) -> int:    

        def helper(root):
            
            if(root):
                if(not root.left and not root.right):
                    return 1
                
                if(not root.left and root.right):
                    return 1 + helper(root.right)
                
                if(not root.right and root.left):
                    return 1 + helper(root.left)
                
                return 1 + min(helper(root.left), helper(root.right))
            return 0

        return(helper(root))

if __name__ == '__main__':

    # tree = TreeNode(3)
    # tree.left = TreeNode(9)
    # tree.right = TreeNode(20)
    # tree.right.left = TreeNode(15)
    # tree.right.right = TreeNode(7)
    # tree.right.left.left = TreeNode(20)

    TN = TreeNode

    tree = TN(2)
    tree.right = TN(3)
    tree.right.right = TN(4)
    tree.right.right.right= TN(5)


    obj = Solution()
    print(obj.minDepth(tree))
