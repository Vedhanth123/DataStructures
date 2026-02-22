class Solution:
    def mySqrt(self, x: int) -> int:
        
        left = 1
        right = 2**16
        answer = [0]

        '''
        while(left <= right):

            mid = left + (right - left) // 2
            if(mid * mid <= x):
                answer = max(answer, mid)
                left = mid + 1
            else:
                right = mid - 1
        '''
        
      

    # let's try recursion version of the sqrt
        def helper(left, right):

            if(left <= right):
                mid = left + (right - left) // 2
                if(mid * mid <= x):
                    answer[0] = max(answer[0], mid)
                    helper(mid + 1, right)
                else:
                    helper(left, mid - 1)
        
        helper(left, right)
        return answer[0]
        
        

    
print(Solution().mySqrt(x=9))