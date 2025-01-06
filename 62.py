class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n] * m
        for v in range(m):
            for u in range(n):
                if u == 0 and v == 0:
                    grid[v][u] = 1
                elif u == 0:
                    grid[v][u] = grid[v-1][u]
                elif v == 0:
                    grid[v][u] = grid[v][u-1]
                else:
                    grid[v][u] = grid[v-1][u] + grid[v][u-1]
        return grid[-1][-1]