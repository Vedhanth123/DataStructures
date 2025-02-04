class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # start from the top left of the array



        # return 1

        # again come back to point 1 and repeat

        
        def helper(row, col):

            if(row == len(grid) or col == len(grid[0]) or row == -1 or col == -1 or grid[row][col] == '0'):
                return


            grid[row][col] = '0'
            helper(row+1,col)
            helper(row-1,col)
            helper(row,col+1)
            helper(row,col-1)

            return 1


        count = 0
        # start from the top left of the array
        for x in range(len(grid)):
            for y in range(len(grid[x])):

                # search for ones in the array
                # if one is found then check the path till you reach zero
                # also mark the points zero while you are travelling
                if(grid[x][y] == '1'):
                    print(x,y, grid[x][y])
                    count += helper(x,y)
        
        return count




