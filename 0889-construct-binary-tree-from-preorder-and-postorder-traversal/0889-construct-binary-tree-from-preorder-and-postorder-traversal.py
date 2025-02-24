

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        
        root = TreeNode(preorder[0])  # First element of preorder is the root
        if len(preorder) == 1:  
            return root  # If only one element, return as root
        
        left_root_val = preorder[1]  # Left child is the next in preorder
        left_subtree_size = postorder.index(left_root_val) + 1  # Size of left subtree

        # Construct left and right subtrees
        root.left = self.constructFromPrePost(preorder[1:left_subtree_size+1], postorder[:left_subtree_size])
        root.right = self.constructFromPrePost(preorder[left_subtree_size+1:], postorder[left_subtree_size:-1])
        
        return root
