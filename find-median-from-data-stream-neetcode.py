class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        if self.large and -1 * self.small[0] > self.large[0]:
            temp = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * temp)
        if len(self.small) > len(self.large) + 1:
            temp = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * temp)
        if len(self.small) +1 < len(self.large):
            temp = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * temp)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0])/2
        
        