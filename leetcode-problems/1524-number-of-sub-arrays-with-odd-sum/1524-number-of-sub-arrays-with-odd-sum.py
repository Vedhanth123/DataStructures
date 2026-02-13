class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        # prefix_sum of [0] -> this is even andhuke so even eppudu 1 ah vuntadhi

        prefix_sum = [arr[0]] * len(arr)

        for x in range(1,len(arr)):
            prefix_sum[x] = prefix_sum[x-1] + arr[x] 
        
        result = 0
        even_count = 1
        odd_count = 0

        for x in range(len(prefix_sum)):

            if(prefix_sum[x]%2 ==0):
                result=(result+odd_count)
                even_count+=1
            else:
                result=(result+even_count)
                odd_count+=1
        
        return result % (10**9 + 7)