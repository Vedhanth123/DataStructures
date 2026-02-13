# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def helper(root, inorder, postorder):

            if(len(inorder) == 0):
                return None
            
            else:
                # [2,1,3]
                root = TreeNode(postorder[-1])
                index = inorder.index(postorder.pop())

                root.right = helper(root.right, inorder[index+1:], postorder)
                root.left = helper(root.left, inorder[:index], postorder)
            
                return root
        
        root = helper(None, inorder, postorder)
        return root