class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        number_to_letter = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        answer = []

        def helper(digits,index, subset):

            if(index == len(digits)):
                if(len(subset) >= 1):
                    answer.append("".join(subset.copy()))
                return
            
            for x in number_to_letter[digits[index]]:
                subset.append(x)
                helper(digits,index+1,subset)
                subset.pop()
        
        helper(digits,0,[])
        return answer

            



