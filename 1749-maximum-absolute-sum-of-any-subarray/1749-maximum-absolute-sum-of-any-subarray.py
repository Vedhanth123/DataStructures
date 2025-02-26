class Solution:

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        def dfs(index, sum_, answer):

            if(index == len(nums)):
                answer = max(answer, abs(sum_))
                return answer
            
            answer = max(answer, abs(sum_+nums[index]))
            answer = max(answer, dfs(index+1, sum_+nums[index], answer))
            
            return answer
                
                
        res = 0
        for x in range(len(nums)):

            res = max(res, dfs(x, 0, res))
        
        return res