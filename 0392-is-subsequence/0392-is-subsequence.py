class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        ptr = 0
        if(len(s) == 0):
            return True

        for x in range(len(t)):

            if(s[ptr] == t[x]):
                ptr += 1
                
                if(ptr == len(s)):
                    return True
        
        return False