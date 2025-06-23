# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        stack1 = []
        stack2 = []

        stack3 = []

        p1 = l1
        p2 = l2

        while(p1):
            stack1.append(p1.val)
            p1 = p1.next
        
        while(p2):
            stack2.append(p2.val)
            p2 = p2.next
        
        carry = 0
        while(stack1 and stack2):
            sum_ = stack1.pop() + stack2.pop() + carry
            carry = 1 if sum_ >= 10 else 0
            stack3.append(sum_ % 10)
        
        while(stack1):
            sum_ = stack1.pop() + carry
            carry = 1 if sum_ >= 10 else 0
            stack3.append(sum_ % 10)

        while(stack2):
            sum_ = stack2.pop() + carry
            carry = 1 if sum_ >= 10 else 0
            stack3.append(sum_ % 10)
        
        if(carry):
            stack3.append(carry)

        answer = ListNode()
        temp = answer

        while(stack3):
            temp.next = ListNode(stack3.pop())
            temp = temp.next
        
        return answer.next
            
