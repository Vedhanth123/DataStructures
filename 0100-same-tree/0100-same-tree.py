# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        preorder = []

        def inorder(root,ino):
            if(root):
                inorder(root.left,ino)
                ino.append(root.val)
                inorder(root.right,ino)
            else:
                ino.append(None)
            return ino
        
        def preorder(root,pre):
            if(root):
                pre.append(root.val)
                preorder(root.left,pre)
                preorder(root.right,pre)
            else:
                pre.append(None)
            return pre
        
        ip = inorder(p, [])
        iq = inorder(q, [])
        pp = preorder(p, [])
        pq = preorder(q, [])
    
        return ((ip == iq) and (pp == pq))