def getInversions(arr, n):
    # write your code here !!

    def helper(left, right):

        if left + 1 >= right:
            return 0

        mid = (left + right) // 2
        left_count = helper(left, mid)
        right_count = helper(mid, right)

        left_arr = arr[left:mid]
        right_arr = arr[mid:right]

        count = 0
        lptr = 0
        rptr = 0

        while lptr < len(left_arr) and rptr < len(right_arr):
            if left_arr[lptr] > right_arr[rptr]:
                count += len(left_arr) - lptr
                rptr += 1
            else:
                lptr += 1

        # now sort the array tooo.
        k = left
        lptr = 0
        rptr = 0
        while lptr < len(left_arr) and rptr < len(right_arr):
            if left_arr[lptr] < right_arr[rptr]:
                arr[k] = left_arr[lptr]
                lptr += 1
                k += 1
            else:
                arr[k] = right_arr[rptr]
                rptr += 1
                k += 1

        while lptr < len(left_arr):
            arr[k] = left_arr[lptr]
            lptr += 1
            k += 1

        while rptr < len(right_arr):
            arr[k] = right_arr[rptr]
            rptr += 1
            k += 1

        return count + left_count + right_count

    return helper(0, n)


print(getInversions([5, 3, 2, 4, 1], 5))
