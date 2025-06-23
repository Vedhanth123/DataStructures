"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if(not head):
            return 
        
        new_dict = {}
        p1 = head
        while(p1):
            new_dict[p1] = Node(p1.val)
            p1 = p1.next
        
        p1 = head
        while(p1):
            new_dict[p1].next = new_dict.get(p1.next)
            new_dict[p1].random = new_dict.get(p1.random)

            p1 = p1.next
        
        return new_dict[head]