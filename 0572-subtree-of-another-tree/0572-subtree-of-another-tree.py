# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def isSubtree(root, subRoot) -> bool:

        
        def inorder(root, arr):
            
            if(root):
                arr.append(root.val)
                inorder(root.left, arr)
                inorder(root.right, arr)
            else:
                return arr
        
        subRoot_inorder = []

        inorder(subRoot, subRoot_inorder)

        print(subRoot_inorder)

        answer = False
        def finder(root, val):

            if(root.val == val):
                root_inorder = []
                answer = subRoot_inorder == inorder(root, root_inorder)
                return
            finder(root.left, val)
            finder(root.right, val)
    



        
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
    obj.isSubtree(root = root, subRoot = subRoot)
