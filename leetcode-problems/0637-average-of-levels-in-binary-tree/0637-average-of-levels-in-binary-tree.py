# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        answer = []

        if(root):

            queue = deque([root])

            while(queue):
                
                size = len(queue)
                sum_of_level = 0

                for x in range(len(queue)):
                
                    curr = queue.popleft()
                    sum_of_level += curr.val

                    if(curr.left):
                        queue.append(curr.left)
                    if(curr.right):
                        queue.append(curr.right)
                
                answer.append(sum_of_level/size)
        
        return answer


        