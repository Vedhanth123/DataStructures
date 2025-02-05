# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        # level order traversal of binary tree
        answer = []

        if(root):
            queue = [root]
            answer = []

            while(queue):
                level = []

                size = len(queue)
                level_sum = 0
                for x in range(len(queue)):
                    curr = queue.pop(0)
                    level_sum += curr.val
                    if(curr.left):
                        queue.append(curr.left)
                    if(curr.right):

                        queue.append(curr.right)

                answer.append(level_sum / size)
                
        
        return answer
