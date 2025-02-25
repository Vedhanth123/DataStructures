class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
    
        res = 0

        def dfs(index, summer):

            if(index == len(arr)):
                if(summer % 2 == 1):
                    return 1
                else:
                    return 0
            
            count = 0
            if(summer % 2 == 1):
                count = 1
            
            count += dfs(index+1, summer + arr[index])
            return count


        for x in range(len(arr)):

            res += dfs(x, 0)
        
        return res