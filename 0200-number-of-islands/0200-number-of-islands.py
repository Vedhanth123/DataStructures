class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        queue = []

        islands = 0

        directions = [(0,-1), (0,1), (1,0), (-1,0)]
        for x in range(len(grid)):
            for y in range(len(grid[0])):

                if(grid[x][y] == '1'):
                    queue.append((x,y))
                    islands += 1

                    while(queue):

                        curr = queue.pop(0)

                        for r, c in directions:

                            if(0<= curr[0]+r < len(grid) and 0 <= curr[1]+c <len(grid[0]) and grid[curr[0]+r][curr[1]+c] == '1'):

                                queue.append((curr[0]+r, curr[1]+c))
                                grid[curr[0]+r][curr[1]+c] = 0
        

        return islands




