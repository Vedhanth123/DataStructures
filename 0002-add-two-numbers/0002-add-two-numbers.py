# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sum_ = 0
        carry = 0

        p1 = l1
        p2 = l2

        new_head = ListNode()
        temp = new_head

        while(p1 and p2):

            sum_ = p1.val + p2.val + carry
            if(sum_ >= 10):
                carry = 1
            else:
                carry = 0

            temp.next = ListNode(sum_ % 10)
            temp = temp.next
            p1 = p1.next
            p2 = p2.next

        while(p1):
            
            sum_ = p1.val + carry
            if(sum_ >= 10):
                carry = 1
            else:
                carry = 0
            
            temp.next = ListNode(sum_ % 10)
            temp = temp.next
            p1 = p1.next
        
        while(p2):

            sum_ = p2.val + carry
            if(sum_ >= 10):
                carry = 1
            else:
                carry = 0
            
            temp.next = ListNode(sum_ % 10)
            temp = temp.next
            p2 = p1.next

        
        if(carry):
            temp.next = ListNode(carry)
            temp = temp.next

        return new_head.next