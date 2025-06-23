# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder(self, tree, inorder):

        if(tree):
            self.inorder(tree.left, inorder)
            inorder.append(tree.val)
            self.inorder(tree.right, inorder)
        else:
            inorder.append(None)
        return inorder

    def preorder(self, tree, preorder):
        if(tree):
            preorder.append(tree.val)
            self.preorder(tree.left, preorder)
            self.preorder(tree.right, preorder)
        else:
            return preorder.append(None)
        return preorder

    def postorder(self, tree, postorder):
        if(tree):
            postorder.append(tree.val)
            self.postorder(tree.left, postorder)
            self.postorder(tree.right, postorder)
        else:
            return postorder.append(None)
        return postorder

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        return self.inorder(p, []) == self.inorder(q, []) and self.preorder(p, []) == self.preorder(q, [])