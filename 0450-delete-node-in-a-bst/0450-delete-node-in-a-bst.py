# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:


        # lc-max
        # rc-min

        def find_min(root):
            while(root and root.left):
                root = root.left
            
            return root

        def delete(root, key):

            if(root):

                if(key == root.val):

                    # 1) no children or leaf
                    if(root.left == None and root.right == None):
                        return None
                    elif(root.left != None and root.right == None):
                        return root.left
                    elif(root.left == None and root.right != None):
                        return root.right
                    else:
                        mi = find_min(root.right)
                        mi.right = delete(root.right, mi.val)
                        mi.left = root.left
                        return mi
                    
                
                if(key < root.val):
                    root.left = delete(root.left , key)

                if(key > root.val):
                    root.right = delete(root.right, key)

            return root
        
        return delete(root, key)