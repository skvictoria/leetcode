class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        whole_sum = sum(nums)
        for pivot in range(len(nums)):
            
            if left == whole_sum - nums[pivot] - left:
                return pivot
            left += nums[pivot]
        return -1
