class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if(len(s) != len(goal)):
            return False 
        for starting_index in range(len(s)):
            count = 0
            for x in range(len(s)):
                if(s[x] == goal[starting_index % len(goal)]):
                    count += 1
                starting_index += 1
            if(count == len(s)):
                return True
        
        return False
    