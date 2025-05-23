class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = 0
        for i in range(k):
            max_sum += nums[i]
        track_num = max_sum
        for i in range(0, len(nums)-k):
            if max_sum <= nums[i+k] - nums[i] + track_num:
                max_sum = track_num + nums[i+k] - nums[i]
            track_num += (nums[i+k] - nums[i])
        return max_sum / k
