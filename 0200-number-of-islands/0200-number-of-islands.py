class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, x, y):
            adj = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            for i in adj:
                x1 = x+i[0]
                y1 = y+i[1]
                if x1>=0 and x1<len(grid) and y1>=0 and y1<len(grid[0]) and grid[x1][y1]=='1':
                    grid[x1][y1] = '0'
                    dfs(grid, x1, y1)
        iceland = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    iceland+=1
                    dfs(grid, i,j)
        return iceland