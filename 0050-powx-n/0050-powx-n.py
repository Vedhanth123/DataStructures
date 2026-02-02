class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # positive n
        def rec(x,n):

            if(n == 0):
                return 1
            return x * rec(x,n-1)

        
        if(n < 0):
            return 1/rec(x,-n)
        else:
            return rec(x,n)

Solution().myPow(x = 2.00000, n = -2)
        