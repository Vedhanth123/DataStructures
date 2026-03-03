def findLargestMinDistance(boards: list, k: int):
    # Write your code here
    # Return an integer
    pass

    # Let's start from the bare minimum thing.
    # If I consider allowing painters to paint only 1 unit of area then the no. of painters needed will increase.
    # If I keep on increasing then I will somehow find out a way that with so and so area I will have the reamining no. of painters

    left = min(boards)
    right = sum(boards)

    while(left <= right):
        mid = left + (right - left) // 2

        painters = 1
        painter_area = 0
        localAnswer = float('-inf')
        for board in boards:

            if painter_area + board > mid:
                painters += 1
                localAnswer = max(localAnswer, painter_area)
                painter_area = board
            else:
                painter_area += board

        if painters >= k:
            left = mid + 1
        else:
            right = mid - 1

    return left



findLargestMinDistance([10, 20, 30, 40], 2)
