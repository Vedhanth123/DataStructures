class Solution:
    def permute(self, nums):
        

        ans = []
        def helper(nums, index, arr, included):

            if(index == len(nums)):
                ans.append(arr.copy())
                return
            

            for x in range(len(nums)):

                if(nums[x] not in included):
                    arr.append(nums[x])
                    included.add(nums[x])
                    helper(nums, index+1, arr, included)
                    arr.pop()
                    included.remove(nums[x])
            
        
        helper(nums, 0, [], set())
        return ans


if __name__ == '__main__':
    
    obj = Solution()
    obj.permute([1,2,3])


