# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        new_list = ListNode()
        temp = new_list

        p1 = l1
        p2 = l2

        carry = 0

        while(p1 and p2):

            sum_ = p1.val + p2.val + carry
            carry = 1 if sum_ >= 10 else 0
            temp.next = ListNode(sum_%10)
            temp = temp.next
            p1 = p1.next
            p2 = p2.next
        
        while(p1):
            sum_ = p1.val + carry
            carry = 1 if sum_ >= 10 else 0
            temp.next = ListNode(sum_%10)
            temp = temp.next
            p1 = p1.next

        while(p2):

            sum_ = p2.val + carry
            carry = 1 if sum_ >= 10 else 0
            temp.next = ListNode(sum_%10)
            temp = temp.next
            p2 = p2.next

        if(carry):
            temp.next = ListNode(carry)
    
        
        return new_list.next

