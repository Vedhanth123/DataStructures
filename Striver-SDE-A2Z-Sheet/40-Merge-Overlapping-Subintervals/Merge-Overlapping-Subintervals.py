from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # let's find the minimum and maximum in the intervals
        intervals.sort()

        answers = [intervals[0]]
        for start,end in intervals:
            # print(answers)
            # print(intervals[x][0] >= answers[-1][0])
            # print(answers[-1][1] <= intervals[x][1])
            if(answers[-1][0] <= start <= answers[-1][1]):
                # print("merge")
                answers[-1][0] = min(answers[-1][0], start)
                answers[-1][1] = max(answers[-1][1], end)
            else:
                answers.append([start,end])
            
        return answers          

Solution().merge(intervals = [[1,3],[2,6],[15,18],[8,10]])