# Algorithm: BFS
'''
for u in range(m):
for v in range(n):
chk[]: if the region is previously searched/not
if it is not chk[] and if it is 1:
BFS()
calculateArea
numberofImage
'''

# Time complexity: O(mn)
# Data structure:
'''
graph: int[][]
chk[][]
bfs: queue
'''
import sys

def BFS(y,x):
    num_of_area = 1
    q = [(y,x)]

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    while q:
        qy, qx = q.pop()
        for loc in range(4):
            x = qx + dx[loc]
            y = qy + dy[loc]
            if 0<=y<n and 0<=x<m and map[y][x] is 1 and check[y][x] is False:
                q.append((y,x))
                check[y][x] = True
                num_of_area += 1
    return num_of_area

input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
check = [[False]*m for _ in range(n)]
num_of_image = 0
max_of_area = 0

for v in range(n):
    for u in range(m):
        if check[v][u] is False and map[n][m] is 1:
            
            check[v][u] = True
            max_of_area = max(BFS(v, u), max_of_area)
            num_of_image += 1
print(num_of_image)
print(max_of_area)