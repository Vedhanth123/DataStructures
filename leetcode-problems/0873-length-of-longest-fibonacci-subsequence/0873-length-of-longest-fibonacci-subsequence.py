class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        total_len = 0

        dp = [[0] * len(arr) for _ in range(len(arr))]

        val_to_idx = defaultdict(int)

        for x in range(len(arr)):
            val_to_idx[arr[x]] = x

        for i in range(len(arr)):
            for j in range(i):

                diff = arr[i] - arr[j]
                idx = val_to_idx.get(diff,-1)

                if(diff < arr[j] and idx >= 0):
                    dp[j][i] = dp[idx][j] + 1
                else:
                    dp[j][i] = 2
                
                total_len = max(total_len, dp[j][i])
        
        return total_len if total_len > 2 else 0

                    
