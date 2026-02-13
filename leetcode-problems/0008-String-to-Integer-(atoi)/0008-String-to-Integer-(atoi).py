class Solution:
    def myAtoi(self, s: str) -> int:
        
        
        # ---------------------------------------------- OBSERVATION -------------------------------------------------------------------
        # 1) Check the first character in the problem.
        # 2) If the first character is '-' then negative number else '+' or nothing. I mean if non zero digit starts then positive number
        # 3) The recursion will continue till there are numeric characters
        # 4) If the length of the string exceeds then stop or if the the character arrives then stop...

        # ---------------------------------------------- ALGORITHM ---------------------------------------------------------------
        # 0) Check for the polarity of the character
        # 1) create a function which will iterate over the given string
        # 2) Base cases: If the index exceeds the length of the string then return None or if the character is non numeric
        # 3) num * 10 + rec(i+1)

        def rec(i,ctr):

            if(i >= len(s) or not s[i].isnumeric()):
                return (0,0)

            if(ctr == 0 and s[i] == '0'):
                return rec(i+1, ctr)

            ans,mu = rec(i+1, ctr+1)

            ans = int(s[i]) * (10**mu) + ans
            if(ans <= 2**31):
                return ans,mu+1
            else:
                return 2**31,mu+1
                
        i = 0
        while(i < len(s) and s[i] == ' '):
            i += 1
        
        if(i < len(s)):
            if(s[i] == '-'):
                answer = -1 * rec(i+1,0)[0]
            elif(s[i] == '+'):
                answer = rec(i+1,0)[0]
            else:
                answer = rec(i,0)[0]

            if(answer >= 2**31):
                answer -= 1
            return answer
        else:
            return 0
            

Solution().myAtoi(' -00123')