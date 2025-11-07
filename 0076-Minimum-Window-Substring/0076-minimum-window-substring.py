from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if(len(t) > len(s)):
            return ""

        left = 0
        answer = ""
        min_length = float('inf')
        freqT = defaultdict(int)
        freqS = defaultdict(int)

        for c in t:
            freqT[c] += 1

        for right in range(len(s)):

            freqS[s[right]] += 1

            mistake = False
            for key,val in freqT.items():
                if(freqT[key] > freqS[key]):
                    mistake = True
                    break
            
            if(not mistake):

                while(left <= right and not mistake):

                    if(right - left + 1 < min_length):
                        min_length = right - left + 1
                        answer = s[left:right+1]
                    freqS[s[left]] -= 1
                    left += 1
                    mistake = False
                    for key,val in freqT.items():
                        if(freqT[key] > freqS[key]):
                            mistake = True
                            break
                    
                    if(mistake):
                        break

        return answer
        
        
obj = Solution()
obj.minWindow(s = "a", t = "a")