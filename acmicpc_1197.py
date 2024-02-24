'''
algorithm: 
1. save the info into the adjacency list. -> O(E)
2. for all (a,b,c): push into heap. so that I can pop minimum weights first
3. while heap:-> O(E)
    if not checked:
        checked = true
        sum_weight += weight
        push into heap. -> O(logE * E)

O(E) + O(E) + O(E log E) -> O(E log E)

'''

import heapq
import sys

input = sys.stdin.readline

v,e = map(int, input().split())
adj_list = [[] for _ in range(v+1)]
for i in range(e):
    a,b,c = map(int, input().split())
    adj_list[a].append([c,b])
    adj_list[b].append([c,a])

heap = [[0,1]]
sum_weight = 0

checked = [False]*(v+1)
while heap:
    weight, node = heapq.heappop(heap)
    if checked[node] == False:
        checked[node] = True
        sum_weight += weight
        for adj_edge in adj_list[node]:
            if checked[adj_edge[1]] == False:
                heapq.heappush(heap, adj_edge)

print(sum_weight)