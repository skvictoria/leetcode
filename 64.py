class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for rows in range(len(grid)):
            for cols in range(len(grid[rows])):
                if rows == 0 and cols == 0:
                    continue
                elif rows == 0:
                    grid[rows][cols] += grid[rows][cols-1]
                elif cols == 0:
                    grid[rows][cols] += grid[rows-1][cols]
                else:
                    grid[rows][cols] += min(grid[rows][cols-1], grid[rows-1][cols])
        return grid[-1][-1]