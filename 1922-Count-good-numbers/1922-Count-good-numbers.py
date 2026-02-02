class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        def rec(index):

            if(index == n):
                return 1
            
            if(index % 2):
                return 4 * rec(index + 1)
            else:
                return 5 * rec(index + 1)
        
        
        print(rec(0))

Solution().countGoodNumbers(4)