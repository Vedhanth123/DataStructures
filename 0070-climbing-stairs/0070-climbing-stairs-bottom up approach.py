class Solution:
    def climbStairs(self, n: int) -> int:
        
        # def recursion(n):

        #     if(n <= 1):
        #         return 1
        #     else:
        #         return recursion(n-1) + recursion(n-2)

        # return recursion(n)

        # def memoization
        # mem = [1,1] + [-1] * (n-1)
        # def rec2(n):

        #     if(mem[n] != -1):
        #         return mem[n]
        #     else:
        #         mem[n] = rec2(n-1) + rec2(n-2)
        #         return mem[n]
    
        # rec2(n)
        # return mem[n]

        # iteration
        prev1 = 0
        prev2 = 1
        curr = 0
        for x in range(1,n+1):
            curr = prev2 + prev1
            prev1 = prev2
            prev2 = curr
        
        return curr
            