class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        n = len(nums)
        
        fixed = 0
        while fixed < n - 2:
            # skip duplicate fixed values
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                fixed += 1
                continue
            
            lp, rp = fixed + 1, n - 1
            while lp < rp:
                total = nums[fixed] + nums[lp] + nums[rp]
                
                if total == 0:
                    answer.append([nums[fixed], nums[lp], nums[rp]])
                    # skip duplicates on the left
                    while lp < rp and nums[lp] == nums[lp + 1]:
                        lp += 1
                    # skip duplicates on the right
                    while lp < rp and nums[rp] == nums[rp - 1]:
                        rp -= 1
                    # move both pointers inward
                    lp += 1
                    rp -= 1
                    # restart loop with new lp/rp
                    continue
                
                # otherwise move one pointer
                if total < 0:
                    lp += 1
                else:
                    rp -= 1
            
            fixed += 1
        
        return answer