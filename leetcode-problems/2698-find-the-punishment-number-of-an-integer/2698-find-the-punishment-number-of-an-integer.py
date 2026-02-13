class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        '1231'
        def part(i, curr, target, string):
            if(i == len(string) and curr == target):
                return True
            
            for j in range(i, len(string)):
                
                if(part(j+1, curr + int(string[i:j+1]))):
                    return True
            
            return False
        
        res = 0
        for i in range(1,n+1):
            if(part(0,0, i, str(i*i))):
                res += i * i
        
        return res



                


