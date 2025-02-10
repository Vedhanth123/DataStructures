# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        answer = 0
        if(root):

            queue = deque([root])

            while(queue):

                for x in range(len(queue)):
                    curr = queue.popleft()

                    if(curr.left):
                        queue.append(curr.left)
                    if(curr.right):
                        queue.append(curr.right)
                
                answer += 1
            
        return answer

