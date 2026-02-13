class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        answer = 0
        freq = {chr(x):0 for x in range(65, 65+26)}

        for right in range(len(s)):

            freq[s[right]] += 1
            highestFreq = 0

            for x in range(65, 65+26):
                if(freq[chr(x)] > highestFreq):
                    highestFreq = freq[chr(x)]
                    highestFreqChar = chr(x)

            if((right-left+1) - freq[highestFreqChar] > k):
                while((right-left+1) - freq[highestFreqChar] > k):
                    freq[s[left]] -= 1
                    left += 1

                    highestFreq = 0

                    for x in range(65, 65+26):
                        if(freq[chr(x)] > highestFreq):
                            highestFreq = freq[chr(x)]
                            highestFreqChar = chr(x)
                    
                
            answer = max(answer, right - left + 1)
        return answer

obj = Solution()
print(obj.characterReplacement(s = "ABABAB", k = 2))