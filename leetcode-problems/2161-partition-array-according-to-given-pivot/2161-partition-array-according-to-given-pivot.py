class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        small_elements = []

        pivot_elements = []
        for x in range(len(nums)):

            if(nums[x] < pivot):

                heapq.heappush(small_elements, (x,nums[x]))
            
            if(nums[x] == pivot):
                pivot_elements.append(nums[x])

        
        large_elements = []

        for x in range(len(nums)):

            if(nums[x] > pivot):

                heapq.heappush(large_elements, (x,nums[x]))
        
        for x in range(len(nums)):

            if(small_elements):
                ind, val = heapq.heappop(small_elements)
                nums[x] = val
            elif(pivot_elements):
                nums[x] = pivot_elements.pop(0)
            else:
                ind, val = heapq.heappop(large_elements)
                nums[x] = val
        
        return nums
