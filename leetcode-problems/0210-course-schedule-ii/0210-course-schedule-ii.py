class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visited = []

        adj = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]

        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1
        
        queue = deque([])

        for node in range(len(indegree)):

            if(indegree[node] == 0):
                queue.append(node)
        
        while(queue):

            curr = queue.popleft()
            visited.append(curr)
            for neigh in adj[curr]:
                indegree[neigh] -= 1
                if(indegree[neigh] == 0):
                    queue.append(neigh)

        
        if(len(visited) != numCourses):
            return []
        else:
            return visited
        
