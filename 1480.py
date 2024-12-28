class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningsum = [''] * len(nums)
        runningsum[0] = nums[0]
        for i in range(1, len(nums)):
            runningsum[i] = runningsum[i-1] + nums[i]
        return runningsum