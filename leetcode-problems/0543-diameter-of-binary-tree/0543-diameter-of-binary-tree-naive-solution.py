# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def heightOfTree(self, root) -> int:

        if(root):
            return 1 + max(self.heightOfTree(root.left), self.heightOfTree(root.right))
        else:
            return 0
    
    answer = 0
    def diameterOfBinaryTree(self, root) -> int:

        # print(f"height of left subtree {self.heightOfTree(root.left)}")
        # print(f"height of right subtree {self.heightOfTree(root.right)}")
        def helper(root):
            if(root):
                self.answer = max(self.answer, self.heightOfTree(root.left) + self.heightOfTree(root.right))
                helper(root.left)
                helper(root.right)
        
        helper(root)
        return self.answer

if __name__ == '__main__':

    obj = Solution()

    TN = TreeNode
    root = TN(1)
    root.left = TN(2)
    root.right = TN(3)
    root.left.left = TN(4)
    root.left.right = TN(5)

    print(obj.diameterOfBinaryTree(root))
        
        
