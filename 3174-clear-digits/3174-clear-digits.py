class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack = []

        for x in range(len(s)):
            
            if(s[x].isalpha()):
                stack.append(s[x])
            else:
                stack.pop()
        
        return "".join(stack)