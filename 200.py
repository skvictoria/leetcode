class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        num_of_island = 0
        def dfs(curV, curU):
            if(curV<0 or curU<0 or curV>=len(grid) or curU>=len(grid[0]) or grid[curV][curU]=='0'):
                return
            grid[curV][curU] = '0'
            dfs(curV-1, curU)
            dfs(curV+1, curU)
            dfs(curV, curU-1)
            dfs(curV, curU+1)
        
        for V in range(len(grid)):
            for U in range(len(grid[0])):
                if(grid[V][U]=='1'):
                    num_of_island += 1
                    dfs(V,U)
        return num_of_island