class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def rec(x,n):
            
            if(n == 0):
                return 1

            if(n % 2 == 0):
                return rec(x*x, n//2)
            else:
                return x * rec(x,n-1)


        if(n < 0):
            return 1 / rec(x,abs(n))
        else:
            return rec(x,n)

        
Solution().myPow(x = 2.00000, n = 9)
        