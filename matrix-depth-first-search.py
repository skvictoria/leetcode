import numpy as np
class Solution:
    def dfs(self, grid, h, w, grid_flag):
        if h<0 or w<0 or h==len(grid) or w==len(grid[0]):
            return 0
        if grid_flag[h][w] == 1 or grid[h][w] != 0:
            return 0
        if h==len(grid)-1 and w==len(grid[0])-1:
            return 1
        grid_flag[h][w] = 1
        cnt = 0
        cnt += self.dfs(grid, h+1, w, grid_flag)
        cnt += self.dfs(grid, h-1, w, grid_flag)
        cnt += self.dfs(grid, h, w+1, grid_flag)
        cnt += self.dfs(grid, h, w-1, grid_flag)
        grid_flag[h][w] = 0
        return cnt

    def countPaths(self, grid: List[List[int]]) -> int:
        grid_flag = np.zeros((len(grid), len(grid[0])))
        return self.dfs(grid, 0, 0, grid_flag)
