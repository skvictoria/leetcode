'''
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for index in range(1, len(nums)):
            if(dp[index - 1] + nums[index] < nums[index]):
                dp.append(nums[index])
            else:
                dp.append(dp[index - 1] + nums[index])
            
        return max(dp)
    
sol = Solution()
sol.maxSubArray([8,-19,5,-4,20])
            