from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxLeft = []
        maxRight = []

        prefixLeft = height[0]
        suffixRight = height[-1]

        for x in range(len(height)):

            prefixLeft = max(prefixLeft, height[x])
            suffixRight = max(suffixRight, height[len(height)-1-x])

            maxLeft.append(prefixLeft)
            maxRight.append(suffixRight)
    
        print(maxLeft, maxRight)

        maxRight.reverse()
        answer = 0
        for x in range(1, len(height)-1):

            answer += max(0, min(maxLeft[x-1], maxRight[x+1]- height[x]))
        
        return answer
obj = Solution()
obj.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])