class Solution():

    def longestSubarraywithSumK(self, array: list[int], k: int) -> int:

        '''
        answer = 0

        # the optimal solution which the striver has told us to do was to take prefix sum of the array and also maintain a hashmap.

        # The algorithm goes like this.
        # 1) A simple for loop which will be gonig from the left to right
        # 2) You will be maintaining a sum variable which will be summing from the first index to the last
        # 3) At every index will be checking for if(sum_ - k in hashmap): then answer = max(answer, x-hashmap[sum_-k])
        # 4) In english we simply mean that if there exists a sum which is sum_ - k in the hashmap then we find the length from that index to the current index and update our answer

        hashMap = {}
        sum_ = 0
        for x in range(len(array)):
            sum_ += array[x]
            if(sum_ - k in hashMap):
                answer = max(answer, x - hashMap[sum_ - k])
            if(sum_ != sum_ - array[x]):
                hashMap[sum_] = x
    
        return answer
    
    '''
    # two pointer approach.
    # If the sum of the window exceeds k then shrink the sum
        answer = 0
        sum_ = 0
        left = 0
        for right in range(len(array)):
            sum_ += array[right]
            while(left <= right and sum_ > k):
                sum_ -= array[left]
                left += 1
                      
            if(sum_ == k):
                answer = max(answer, right - left + 1)
        
        return answer


     
print(Solution().longestSubarraywithSumK([1,2,3,1,1,1,4,5],3))

        