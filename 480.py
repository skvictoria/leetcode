# class heap:
#     def __init__(self, nums):
#         self.small = []
#         self.large = []
#         self.list = nums

#     def add(self, index):
#         heapq.heappush(self.small, self.list[index])
#         if self.small and self.large and -1 * self.small[0] > self.large[0]:
#             val = heapq.heappop(self.small[0])
#             heapq.heappush(self.large, -1 * val)
#         if len(self.small) > len(self.large) + 1:
#             val = heapq.heappop(self.small[0])
#             heapq.heappush(self.large, -1 * val)
#         elif len(self.small) + 1 < len(self.large):
#             val = heapq.heappop(self.large[0])
#             heapq.heappush(self.small, -1 * val)

#     def getmed(self, index):
#         if len(self.small) > len(self.large):
#             return self.small[0] * -1
#         elif len(self.small) < len(self.large):
#             return self.large[0]
#         else:
#             return self.large[0] - self.small[0]

# class Solution:
#     def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        start = 0
        finish = k
        if k % 2 == 1:
            median1 = int(k / 2)
            median2 = int(k / 2)
        else:
            median1 = int(k / 2) - 1
            median2 = int(k / 2)
        output_list = []
        while finish <= len(nums):
            temp_list = []
            temp_list = sorted(nums[start:finish])
            output_list.append((temp_list[median1] + temp_list[median2])/2)
            start += 1
            finish += 1
        return output_list