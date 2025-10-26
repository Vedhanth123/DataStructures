class Solution:
    def findRedundantConnection(self, edges):

        graph = {x+1:[] for x in range(len(edges))}
        def cycle_detection(graph, node, visited, visiting):

            if(node in visiting):
                return True
            
            visited.add(node)
            visiting.add(node)
            for neighbour in graph[node]:
                if(neighbour not in visited):
                    cycle_detection(graph, neighbour, visited, visiting)
            
            return False
        
        for u,v in edges:

            graph[u].append(v)
            graph[v].append(u)
            answer = cycle_detection(graph, u, set(), set())
            print(answer)
            if(answer):
                return [u,v]
            
if __name__ == "__main__":

    obj = Solution()
    obj.findRedundantConnection(edges = [[1,2],[1,3],[2,3]])

