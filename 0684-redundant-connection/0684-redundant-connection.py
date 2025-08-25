class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        graph = {x+1:[] for x in range(len(edges))}

        def check_path(u, v, visited):

            visited.add(u)
            if(u == v):
                return True

            for neighbour in graph[u]:
                if(neighbour not in visited):
                    if(check_path(neighbour, v, visited)):
                        return True
        
            return False
        
        for u,v in edges:

            if(check_path(u,v, set())):
                return [u,v]

            graph[u].append(v)
            graph[v].append(u)