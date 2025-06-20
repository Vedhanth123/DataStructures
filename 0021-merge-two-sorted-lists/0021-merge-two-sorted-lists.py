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
                temp = ListNode(c1.val)
                c1 = c1.next
                curr.next = temp
                curr = curr.next
            else:
                temp = ListNode(c2.val)
                c2 = c2.next
                curr.next = temp
                curr = curr.next

        while(c1):
            temp = ListNode(c1.val)
            c1 = c1.next
            curr.next = temp
            curr = curr.next

        while(c2):
            temp = ListNode(c2.val)
            c2 = c2.next
            curr.next = temp
            curr = curr.next
        
        return head.next

                