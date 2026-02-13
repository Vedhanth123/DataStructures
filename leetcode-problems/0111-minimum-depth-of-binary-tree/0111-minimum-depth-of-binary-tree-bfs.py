# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root) -> int:    

        answer = 0
        if(not root):
            return answer

        queue = [root]

        while(queue):

            for x in range(len(queue)):
                curr = queue.pop(0)
                if(not curr.left and not curr.right):
                    return answer + 1
                if(curr.left):
                    queue.append(curr.left)
                if(curr.right):
                    queue.append(curr.right)

            
            answer += 1
        
        return answer

if __name__ == '__main__':

    # tree = TreeNode(3)
    # tree.left = TreeNode(9)
    # tree.right = TreeNode(20)
    # tree.right.left = TreeNode(15)
    # tree.right.right = TreeNode(7)
    # tree.right.left.left = TreeNode(20)

    TN = TreeNode

    tree = TN(2)
    tree.right = TN(3)
    tree.right.right = TN(4)
    tree.right.right.right= TN(5)


    obj = Solution()
    print(obj.minDepth(tree))
