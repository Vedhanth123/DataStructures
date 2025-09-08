# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def search(root, p, q):

            if(root):

                if(p.val < root.val and q.val < root.val):
                    return search(root.left, p, q)
                elif(p.val > root.val and q.val > root.val):
                    return search(root.right, p, q)
                else:
                    return root
        
        return search(root, p, q)
                
                

