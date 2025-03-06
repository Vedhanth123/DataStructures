class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for x in range(len(s)):

            if(s[x] == '(' or s[x] == '[' or s[x] == '{'):
                stack.append(s[x])

            if(s[x] == ')'):

                if(len(stack) == 0):
                    return False
                elif(stack[-1] != '('):
                    return False
                else:
                    stack.pop()
                
            elif(s[x] == ']'):

                if(len(stack) == 0):
                    return False
                elif(stack[-1] != '['):
                    return False
                else:
                    stack.pop()


            elif(s[x] == '}'):

                if(len(stack) == 0):
                    return False
                elif(stack[-1] != '{'):
                    return False
                else:
                    stack.pop()
            else:
                pass
                
        if(len(stack) == 0):
            return True
        else:
            return False