class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False

        else:
            d1 = defaultdict(int)
            d2 = defaultdict(int)

            for x in range(len(s)):
                d1[s[x]] += 1
            
            for x in range(len(t)):
                d2[t[x]] += 1
            
            for x in range(len(s)):

                key = s[x]

                if(d1[key] != d2[key]):
                    return False
        
            return True
            

