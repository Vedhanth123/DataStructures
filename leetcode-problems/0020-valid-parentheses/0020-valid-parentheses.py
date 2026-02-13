class Solution:
    def isValid(self, s: str) -> bool:
        
        open_brackets = ['(','{','[']

        stack = []

        for x in range(len(s)):

            if(s[x] in open_brackets):
                stack.append(s[x])
        
            else:
                if(s[x] == ')'):
                    if(len(stack) and stack[-1] != '(' ):
                        return False
                    else:
                        if(len(stack)):
                            stack.pop()
                        else:
                            return False

                if(s[x] == '}'):
                    if(len(stack) and stack[-1] != '{' ):
                        return False
                    else:
                        if(len(stack)):
                            stack.pop()
                        else:
                            return False
                            
                if(s[x] == ']'):
                    if(len(stack) and stack[-1] != '[' ):
                        return False
                    else:
                        if(len(stack)):
                            stack.pop()
                        else:
                            return False

        return not len(stack)
                    