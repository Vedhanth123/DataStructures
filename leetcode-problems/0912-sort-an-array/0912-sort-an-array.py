class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def MergeSort(left, right, array):
            if left < right:  # Remove unnecessary parentheses
                mid = left + (right - left) // 2  # Fixed parentheses
                
                MergeSort(left, mid, array)
                MergeSort(mid + 1, right, array)
                
                left_array = array[left:mid+1]
                right_array = array[mid+1:right+1]
                
                lp = 0
                rp = 0
                mp = left
                
                while lp < len(left_array) and rp < len(right_array):
                    if left_array[lp] <= right_array[rp]:  # Use <= for stability
                        array[mp] = left_array[lp]
                        lp += 1
                    else:
                        array[mp] = right_array[rp]
                        rp += 1
                    mp += 1
                
                while lp < len(left_array):
                    array[mp] = left_array[lp]
                    lp += 1
                    mp += 1
                
                while rp < len(right_array):
                    array[mp] = right_array[rp]
                    rp += 1
                    mp += 1
                
                # REMOVED: return array (this was unnecessary)
        
        MergeSort(0, len(nums) - 1, nums)
        return nums