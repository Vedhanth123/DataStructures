class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permut(nums,index):

            if(index == len(nums)):
                return [[]]
            
            res = []
            perms = permut(nums,index+1)
            for perm in perms:

                for x in range(len(perm)+1):
                    cp = perm.copy()
                    cp.insert(x,nums[index])
                    res.append(cp)
            
            return res

        return permut(nums,0)

            




                


        answer