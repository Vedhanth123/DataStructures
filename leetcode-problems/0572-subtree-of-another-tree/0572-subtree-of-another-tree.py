# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def issametree(self, p, q) -> bool:

        if(not p and not q):
            return True
        if(not p or not q):
            return False
        if(p.val != q.val):
            return False
        return self.issametree(p.left, q.left) and self.issametree(p.right, q.right)
    
    def isSubtree(self, root, subRoot) -> bool:

        if(not root):
            return False
        
        if(self.issametree(root,subRoot) == True):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    

        
if __name__ == '__main__':


    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)

    obj = Solution()
    print(obj.isSubtree(root = root, subRoot = subRoot))
