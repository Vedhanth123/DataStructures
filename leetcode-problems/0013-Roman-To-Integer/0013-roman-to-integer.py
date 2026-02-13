class Solution:
    def romanToInt(self, s: str) -> int:
        
        answer = 0
        romanToInt = {'I' : 1, 
                    'V': 5, 
                    'X': 10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000}
                    
        for x in range(len(s)):

            if(s[x] == 'I'):
                if(x+1 < len(s) and (s[x+1] == 'V' or s[x+1] == 'X')):
                    answer -= 1
                else:
                    answer += romanToInt[s[x]]
            elif(s[x] == 'X'):
                if(x+1 < len(s) and (s[x+1] == 'L' or s[x+1] == 'C')):
                    answer -= 10
                else:
                    answer += romanToInt[s[x]]
            elif(s[x] == 'C'):
                if(x+1 < len(s) and (s[x+1] == 'D' or s[x+1] == 'M')):
                    answer -= 100
                else:
                    answer += romanToInt[s[x]]
            else:
                answer += romanToInt[s[x]]
        
        return answer

if __name__ == "__main__":
    obj = Solution()
    print(obj.romanToInt("I"))
    print(obj.romanToInt("II"))
    print(obj.romanToInt("III"))
    print(obj.romanToInt("IV"))
    print(obj.romanToInt("V"))
    print(obj.romanToInt("MCMXCIV"))

            
                