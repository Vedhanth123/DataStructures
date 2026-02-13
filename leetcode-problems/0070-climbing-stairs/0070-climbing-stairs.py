class Solution:
    def climbStairs(self, n: int) -> int:
        
        p1 = 1
        p2 = 2

        for x in range(3, n+1):
            curr = p1 + p2
            p1 = p2
            p2 = curr

        return curr