from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # find the frequence of the characters in the s1
        freqS1 = defaultdict(int)
        for x in range(len(s1)):
            freqS1[s1[x]] += 1
        
        freqS2 = defaultdict(int)
        left = 0
        right = 0
        for x in range(len(s1)):
            freqS2[s2[x]] += 1
            right = x

        for x in range(97, 97+26):
            if(freqS1[chr(x)] != freqS2[chr(x)]):
                break

        for x in range(right+1, len(s2)):

            notFound = False
            freqS2[s2[left]] -= 1
            left += 1
            freqS2[s2[x]] += 1

            for x in range(97, 97+26):
                if(freqS1[chr(x)] != freqS2[chr(x)]):
                    notFound = True
                    break
            
            if(not notFound):
                return True
            
        return False


obj = Solution()
obj.checkInclusion(s1 = "ab", s2 = "eidbaooo")
            



        


