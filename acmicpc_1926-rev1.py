'''
algorithm: bfs

num_of_image
area

loop through for loop, if 1 and if not checked -> go to that index and do bfs.
    while doing bfs, change the num_of_image and area.

'''

import sys

num_of_image = 0
maxv = 0

input = sys.stdin.readline
n,m = map(int, input().split())
checked = [[0]*m for _ in range(n)]
image = [list(map(int, input().split())) for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
def bfs(v, u):
    if v<0 or v>=n or u<0 or u>=m:
        return 0
    area_val = 1
    stack = [(v, u)]
    
    
    checked[v][u] = 1
    while stack:
        v_start,u_start = stack.pop()
        for idx in range(4):
            v_change = v_start + dy[idx]
            u_change = u_start + dx[idx]
            if(0<=v_change < n and 0<=u_change < m and image[v_change][u_change] == 1 and checked[v_change][u_change] == 0):
                area_val += 1
                checked[v_change][u_change] = 1
                stack.append((v_change, u_change))
    return area_val


for v in range(n):
    for u in range(m):
        if image[v][u] == 1 and checked[v][u] == 0:
            checked[v][u] = 1
            maxv = max(maxv, bfs(v, u))
            num_of_image += 1
print(num_of_image)
print(maxv)