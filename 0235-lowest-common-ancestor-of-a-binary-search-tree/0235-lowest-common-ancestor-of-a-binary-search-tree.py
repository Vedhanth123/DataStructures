# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def rec(root, p, q):

            if(root):
                if(p < root.val and q < root.val):
                    return rec(root.left, p, q)
                elif(p > root.val and q > root.val):
                    return rec(root.right, p, q)
                else:
                    return root
            
            else:
                return None
        

        return rec(root, p.val, q.val)