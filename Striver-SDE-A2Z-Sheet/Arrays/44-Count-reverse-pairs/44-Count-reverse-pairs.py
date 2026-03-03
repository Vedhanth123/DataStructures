class Solution:
    def reversePairs(self, nums):

        # To solve this problem we upgrade the mergesort algorithm
        # we split the array into two parts
        # we go on splitting the array till the len of the array is 1
        # we then merge the array
        # while merging the array we check if left_array[i] > right_array[j] * 2 if then we increment the counter

        def rec(left, right):

            if left + 1 >= right:
                return 0

            mid = (left + right) // 2

            left_count = rec(left, mid)
            right_count = rec(mid, right)

            left_array = nums[left:mid]
            right_array = nums[mid:right]

            # let's count the pairs
            pair_count = 0
            lp = 0
            rp = 0
            while(lp < len(left_array) and rp < len(right_array)):
                if(left_array[lp] > 2 * right_array[rp]):
                    pair_count += len(left_array) - lp
                    rp += 1
                else:
                    lp += 1
            
            lp = 0
            rp = 0

            k = left
            while(lp < len(left_array) and rp < len(right_array)):
                if(left_array[lp] < right_array[rp]):
                    nums[k] = left_array[lp]
                    lp += 1
                    k += 1
                else:
                    nums[k] = right_array[rp]
                    rp += 1
                    k += 1
            
            while(lp < len(left_array)):
                nums[k] = left_array[lp]
                lp += 1
                k += 1

            while(rp < len(right_array)):
                nums[k] = right_array[rp]
                rp += 1
                k += 1
            
            return pair_count + left_count + right_count

        return rec(0, len(nums))

print(Solution().reversePairs([6, 4, 1, 2, 7]))
