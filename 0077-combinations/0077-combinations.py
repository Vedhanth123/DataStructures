class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        answer = []

        def rec(i,combs):

            if(len(combs) == k):
                answer.append(combs.copy())
            
            for j in range(i, n+1):
                combs.append(j)
                rec(j+1, combs)
                combs.pop()
        
        rec(1,[])
        return answer