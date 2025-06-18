class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
 
        sp = 0
        for x in range(len(t)):
            if(sp < len(t) and t[x] == s[sp]):
                sp += 1
        
        return sp == len(s)

