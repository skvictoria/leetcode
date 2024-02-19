# algorithm:
'''
for v in N:
  for u in N:
    if check == false and map==1:
      x = x + dx
      y = y + dy
      recur(x,y)
      check = true
'''

# O(n^2)

# data structure
'''
num_of_house = int[]
map = int[][]
check = bool[][]
recursive
'''

import sys

def recur(v, u):
    global num_of_house
    num_of_house += 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for d in range(4):
        nv = v + dy[d]
        nu = u + dx[d]
        if 0<=nv<N and 0<=nu<N and check[nv][nu] is False and map[nv][nu] is 1:
            check[nv][nu] = True
            
            recur(nv, nu)
            

input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]
num_of_house = 0
result = []

check = [[False]*N for _ in range(N)]

for v in range(N):
    for u in range(N):
        if check[v][u] is False and map[v][u] == 1:
            num_of_house = 0
            check[v][u] = True
            recur(v,u)
            result.append(num_of_house)

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])