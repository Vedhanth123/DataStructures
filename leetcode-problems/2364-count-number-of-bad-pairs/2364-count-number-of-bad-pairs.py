class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        bad_pairs = 0
        good_pairs = 0

        pairs = defaultdict(int)

        for x in range(len(nums)):

            diff = x - nums[x]
            good_pairs = pairs[diff]

            bad_pairs += x - good_pairs
            pairs[diff] = good_pairs + 1
        
        return bad_pairs