import numpy as np

class WaymoRouteOptimizer:

    def __init__(self, map_grid):
        self.map_grid = map_grid
        self.rows = len(map_grid)
        self.cols = len(map_grid[0])
        self.moves = [(0,1), (1,0), (0,-1), (-1,0)]

    def is_valid(self, x, y):
        flag = False
        
        if((0<= x < self.rows) and (0<=y < self.cols) and self.map_grid[x][y] != 'X'):
            flag = True
        return flag

    def optimize_route(self, start, destination):
        """
        Implement the chosen algorithm from Part 1 to optimize the route
        between the start and destination.
        
        :param start: A tuple representing the starting position (x, y).
        :param destination: A tuple representing the destination position (x, y).
        :return: A list of tuples representing the optimized path.
        """
        # Pseudo-code:
        # 1. Initialize necessary data structures.
        # 2. Check for boundary conditions (like if start is same as destination).
        # 3. Implement the chosen algorithm to find the path.
        # 4. Return the optimized path.

        # initialize distance grid with inifinity and backtracking grid
        distance = np.full((self.rows, self.cols), float('inf'))
        backtrack = np.full((self.rows, self.cols), None)
        distance[start[0]][start[1]] = 0

        for _ in range(self.rows*self.cols):
            for x in range(self.rows):
                for y in range(self.cols):
                    for dx, dy in self.moves:
                        nx, ny = x+dx, y+dy
                        if self.is_valid(nx,ny) and distance[nx][ny] > distance[x][y] + 1:
                            distance[nx][ny] = distance[x][y] + 1
                            backtrack[nx][ny] = (x,y)
                            print("distance : ",distance)
                            print("backtrack : ", backtrack)

        # reconstruct path using backtracking
        path = []
        current = destination
        while current != start:
            path.append(current)
            current = backtrack[current[0]][current[1]]
        path.append(start)
        return path[::-1]

INF = 1000000
# Sample code to test your implementation
map_grid = np.array([
    ['S', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['O', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'X', 'O'],
    ['O', 'O', 'O', 'O', 'D']
])
optimizer = WaymoRouteOptimizer(map_grid)

path = optimizer.optimize_route((0, 0), (4, 4))
print(path)