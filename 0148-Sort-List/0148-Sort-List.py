class Solution:

    def sort(self, left, right):
        
        if(left != right):

            leftEnd, rightStart = self.findMid(left, right)
            self.sort(left,leftEnd)
            self.sort(rightStart,right)

            newNode = ListNode()
            temp = newNode
            leftPtr = left
            rightPtr = rightStart

            while(leftPtr != rightStart and rightPtr != right.next):
                
                if(leftPtr.val <= rightPtr.val):
                    temp.next = ListNode(leftPtr.val)
                    temp = temp.next
                    leftPtr = leftPtr.next
                else:
                    temp.next = ListNode(rightPtr.val)
                    temp = temp.next
                    rightPtr = rightPtr.next
            
            while(leftPtr != rightStart):
                temp.next = ListNode(leftPtr.val)
                temp = temp.next
                leftPtr = leftPtr.next
            
            while(rightPtr != right.next):
                temp.next = ListNode(rightPtr.val)
                temp = temp.next
                rightPtr = rightPtr.next
            
            temp = newNode.next
            insertPtr = left
            while(temp):
                insertPtr.val = temp.val
                temp = temp.next
                insertPtr = insertPtr.next

    def findMid(self, start, end):

        slow = start
        fast = start
        prev = start
        while(fast != end.next and fast.next != end.next):
            prev = slow
            slow = slow.next
            fast = fast.next.next

        return [prev, slow]

    
    def sortList(self, head):
        
        # 1) Find the end of the linked list
        left = head
        fast = head
        prev = None

        while(fast and fast.next):
            prev = fast.next
            fast = fast.next.next
        
        if(fast):
            self.sort(left, fast)
        else:
            self.sort(left, prev)

        return head
