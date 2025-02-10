class Solution:
    def clearDigits(self, s: str) -> str:
        
        # 2) excluded indices
        sett = SortedSet()

        # 1) find the digit
        for x in range(len(s)):

            if(s[x].isnumeric()):
                sett.add(x)
                y = x-1
                for y in range(x-1,-1,-1):
                    if(y not in sett and s[y].isalpha()):
                        sett.add(y)
                        break
        
        answer = ""

        for x in range(len(s)):
            if(x not in sett):
                answer += s[x]
        
        return answer
