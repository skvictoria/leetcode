class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([[rooms[0], 0]])
        visited = [0] * len(rooms)
        visited[0] = 1
        while queue:
            room, index = queue.popleft()
            
            visited[index] = 1
            for num in room:
                if not visited[num]:
                    queue.append([rooms[num], num])
        if sum(visited) == len(rooms):
            return True
        else:
            return False