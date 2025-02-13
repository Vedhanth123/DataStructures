class Solution:
    def climbStairs(self, n: int) -> int:
        
        # def recursion(n):

        #     if(n <= 1):
        #         return 1
        #     else:
        #         return recursion(n-1) + recursion(n-2)

        # return recursion(n)

        # def memoization
        mem = [1,1] + [0] * (n-2)
        def rec2(n):

            if(mem[n] != -1):
                return mem[n]
            else:
                mem[n] = rec2(n-1) + rec2(n-2)
                return mem[n]
    
        return rec2(n)
            