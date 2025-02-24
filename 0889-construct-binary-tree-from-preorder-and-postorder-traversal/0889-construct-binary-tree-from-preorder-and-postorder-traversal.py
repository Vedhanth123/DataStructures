# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def build(preorder, postorder, root):

            if(len(preorder) < 1 and len(postorder) < 1):
                return None
            
            
            root = TreeNode(preorder[0])
            if(len(preorder) == 1):
                return root

            left_val = preorder[1]
            left_size = postorder.index(left_val) + 1

            root.left = build(preorder[1:left_size+1], postorder[:left_size], root.left)
            root.right = build(preorder[left_size+1:], postorder[left_size:-1], root.right)

            return root
        
        return build(preorder, postorder, None)



