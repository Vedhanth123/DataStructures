class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        answer = []

        def backtracking(ptr, sum_, arr):

            if(sum_ == target):
                answer.append(arr.copy())
                return 
            
            if(ptr >= len(candidates) or sum_ > target):
                return

            arr.append(candidates[ptr])
            backtracking(ptr+1, sum_+candidates[ptr], arr)
            arr.pop()

            while(ptr+1 < len(candidates) and candidates[ptr] == candidates[ptr+1]):
                ptr += 1
            
            backtracking(ptr+1, sum_, arr)
        
        
        backtracking(0, 0, [])
        return answer
                