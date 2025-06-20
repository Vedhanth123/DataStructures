# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        curr = head

        c1 = list1
        c2 = list2

        while(c1 and c2):
            
            if(c1.val <= c2.val):
                curr.next = ListNode(c1.val)
                c1 = c1.next
                curr = curr.next
            else:
                curr.next = ListNode(c2.val)
                c2 = c2.next
                curr = curr.next

        while(c1):
            curr.next = ListNode(c1.val)
            c1 = c1.next
            curr = curr.next

        while(c2):
            curr.next = ListNode(c2.val)
            c2 = c2.next
            curr = curr.next
        
        return head.next

                