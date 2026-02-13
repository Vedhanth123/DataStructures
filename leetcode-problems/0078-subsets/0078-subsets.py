class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        def backtracking(nums,index, subset):

            if(index == len(nums)):
                answer.append(subset.copy())
            else:
                subset.append(nums[index])
                backtracking(nums,index+1,subset)
                subset.pop()
                backtracking(nums,index+1,subset)
        
        backtracking(nums,0,[])
        return answer