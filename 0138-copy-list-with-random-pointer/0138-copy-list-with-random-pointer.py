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
            return None
            
        new_list = {}

        curr = head
        while(curr):
            new_list[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while(curr):
            new_list[curr].next = new_list.get(curr.next)
            new_list[curr].random = new_list.get(curr.random)
            curr = curr.next
        
        return new_list[head]