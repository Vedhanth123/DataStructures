# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if(head and head.next):
            temp = head
            length = 0
            while(temp):
                temp = temp.next
                length += 1
            
            indexToRemove = length - n

            temp = head
            prev = None
            curr = temp
            while(curr and curr.next and indexToRemove != 0):

                prev = curr
                curr = curr.next
                indexToRemove -= 1
            
            if(prev != None):
                prev.next = curr.next
            else:
                head = head.next
                
            return head
