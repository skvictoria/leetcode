import numpy as np

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        #count = np.zeros((h, w))
        count = [[-1] * w for _ in range(h)]
        count[0][0] = 0
        q = deque()
        q.append((0,0))
        directions = [(1, 0), (-1,0), (0,-1),(0,1)]
        
        while q:
            r,c = q.popleft()
            if r == h-1 and c== w-1:
                return count[r][c]
            for dr, dc in directions:
                if r + dr <0 or c + dc<0 or r + dr>=h or c + dc>=w or grid[r+dr][c+dc] ==1:
                    continue
                if count[r+dr][c+dc] == -1:
                    count[r+dr][c+dc] = count[r][c] + 1
                    q.append((r+dr, c+dc))
        return -1
