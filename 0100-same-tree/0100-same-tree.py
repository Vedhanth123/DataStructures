# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
    
        def helper(p, q):

            if(not p and not q):
                return True
            if(not p or not q):
                return False
            if(p.val != q.val):
                return False
            
            return helper(p.left, q.left) and helper(p.right, q.right)
    
        print(helper(p, q))

if __name__ == '__main__':


    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(4)

    obj = Solution()
    obj.isSameTree(p, q)
