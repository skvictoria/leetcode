class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # 1. make adjacent list
        adj = {}
        for i in range(0, n+1):
            adj[i] = []
        for s,d,w in edges:
            adj[s].append((d,w))

        # 2. meanheap
        shortest = {}
        minHeap = [(0, src)]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (w1+w2, n2))
        for i in range(0, n):
            if i in shortest:
                continue
            else:
                shortest[i] = -1
        return shortest