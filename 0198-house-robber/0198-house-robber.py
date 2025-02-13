class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp={}
        def dfs(index,sum_):

            if(index >= len(nums)):
                return sum_
            
            if (index,sum_) in dp:
                return dp[(index,sum_)]
            

            skip = dfs(index+1,sum_)

            include=dfs(index+2,sum_+nums[index])

            dp[(index,sum_)]=max(skip,include)

            return dp[(index,sum_)]
    
        return dfs(0,0)

 