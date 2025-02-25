class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        answer = 0
        lowest_val = prices[0]

        for x in range(1, len(prices)):

            answer = max(answer, prices[x] - lowest_val)
            lowest_val = min(lowest_val, prices[x])
        
        return answer