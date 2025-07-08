class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def rec(li, n, k, i):
            if len(li) == k:
                answer.append(li.copy())
                return
            
            if i > n:
                return

            for x in range(i, n + 1):
                li.append(x)
                rec(li, n, k, x+1)
                li.pop() 

        rec([], n, k, 1)
        return answer
