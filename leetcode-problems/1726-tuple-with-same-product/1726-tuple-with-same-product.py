class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        product_cnt = defaultdict(int)
        pair_cnt = defaultdict(int)

        for x in range(len(nums)):
            for y in range(x+1,len(nums)):

                pair_cnt[nums[x] * nums[y]] += product_cnt[nums[x] * nums[y]]

                product_cnt[nums[x] * nums[y]] += 1
        

        res = 0
        for key, val in pair_cnt.items():
            res += 8 * val
        
        return res