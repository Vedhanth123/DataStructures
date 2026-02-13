# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        if(head):
            length = 0
            temp = head

            while(temp):
                temp = temp.next
                length += 1

            to_remove = length - n

            prev = None
            curr = head

            while(curr and to_remove):
                prev = curr
                curr = curr.next
                to_remove -= 1
            
            if(prev and curr):
                prev.next = curr.next
            elif(prev and not curr):
                prev.next = None
            else:
                return head.next
            
        return head
