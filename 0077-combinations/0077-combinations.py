class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        combs = []

        def backtracker(n, k, sub, index):

            if(len(sub) == k):
                combs.append(sub.copy())
                return
            if(index > n):
                return
            
            sub.append(index)
            backtracker(n,k,sub,index+1)
            sub.pop()
            backtracker(n,k,sub,index+1)
    
        backtracker(n,k,[],1)
        return combs