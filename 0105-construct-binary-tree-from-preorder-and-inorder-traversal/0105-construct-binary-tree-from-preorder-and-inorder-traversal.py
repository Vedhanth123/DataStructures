# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build(preorder, inorder, root):

            if(preorder and inorder):

                val = preorder.pop(0)
                root = TreeNode(val)
                root.left = build(preorder, inorder[:inorder.index(val)], root.left)
                root.right = build(preorder, inorder[inorder.index(val)+1:], root.right)

            return root
        
        return build(preorder, inorder, None)