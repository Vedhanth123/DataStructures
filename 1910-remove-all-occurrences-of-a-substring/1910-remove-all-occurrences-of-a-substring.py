class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        stack = []
        for x in range(len(s)):

            stack.append(s[x])
            if(len(stack) >= len(part) and "".join(stack[-len(part):]) == part):
                del stack[-len(part):]

        return "".join(stack)