'''
idea
    - backtracking 
    for all nums:
        if not checked 
            select the num
    return recurs()


'''

import sys

def recur(num):
    if num == 

input = sys.stdin.readline()
N,M = map(int, input())

checked = [0]*len(N+1)
res = [0]*len(N+1)
for i in range(N):
    if checked[i] == 0:
