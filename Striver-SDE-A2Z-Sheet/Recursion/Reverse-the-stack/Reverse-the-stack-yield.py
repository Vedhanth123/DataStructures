# This file deals with using yield function to emulate a 2 pointer approach in recursion
# The right pointer (bottom of the stack is a function which will basically go till the end of the stack and wait...)
# The left pointer (top of the stack is a generator which will go from top to bottom by sending the elements at the top of the stack)

from typing import List

class Solution():

    def reverseStack(stack: List[int]):

        def leftPointer(array, index=0):

            if(index >= (len(array)//2)-1):
                return 
            yield index
            leftPointer(array, index+1)


        # I am supposed to reverse the stack but only use push, pop and only use recursion to reverse the stack.
        def rightPointer(array, index):

            if(index == len(array)):
                return

            rightPointer(array, index+1)
            ind = leftPointer(array)
            array[ind], array[index] = array[index], array[ind]

        rightPointer(stack, 0)

Solution().reverseStack([1,2,3,4,5])