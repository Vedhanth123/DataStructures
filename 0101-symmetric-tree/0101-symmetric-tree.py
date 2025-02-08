# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if(root):

            answer = []
            queue = [root]

            while(queue):
                
                level = []
                for x in range(len(queue)):

                    curr = queue.pop(0)

                    if(curr == None):
                        level.append(None)
                        break

                    level.append(curr.val)
                    if(curr.left):
                        queue.append(curr.left)
                    else:
                        queue.append(None)
                    if(curr.right):
                        queue.append(curr.right)
                    else:
                        queue.append(None)

                for x in range(len(level)//2):

                    if(level[x] != level[-(x+1)]):
                        return False
            
            return True
            

                    