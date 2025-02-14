class Solution:
    def rob(self, nums: List[int]) -> int:
        
        mem = [-1] * (len(nums)+1) 

        def solve(nums, index):
            if(index >= len(nums)):
                return 0
            
            if(mem[index] != -1):
                return mem[index]

            steal = nums[index] + solve(nums,index+2)
            skip = solve(nums,index+1)

            mem[index] = max(steal,skip)
            return mem[index]

        return solve(nums,0)

                