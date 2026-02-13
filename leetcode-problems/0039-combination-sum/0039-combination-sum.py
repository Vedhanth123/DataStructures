class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        answer = []

        
        def helper(index, array, currSum):

            if(currSum > target or index >= len(candidates)):
                return
            
            if(currSum == target):
                return answer.append(array.copy())
            
            array.append(candidates[index])
            helper(index, array, currSum+candidates[index])
            array.pop()
            helper(index+1, array, currSum)
        
        helper(0, [], 0)
        return answer



