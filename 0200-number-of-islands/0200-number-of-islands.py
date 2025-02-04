class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # start from top left part of the grid and search for 1's
        # if found 1 then increment counter
        # do a bfs and change all the values to zero in the coming path
        # return the counter

        islands = 0
        def dfs(row, col, grid):

            if(0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == '1'):

                grid[row][col] = '0'
                dfs(row+1,col, grid)
                dfs(row-1,col, grid)
                dfs(row,col+1, grid)
                dfs(row,col-1, grid)

        for x in range(len(grid)):

            for y in range(len(grid[0])):

                if(grid[x][y] == '1'):
                    dfs(x,y,grid)
                    islands += 1

        
        return islands
                            
