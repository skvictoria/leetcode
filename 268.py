class Solution:
    def missingNumber(self, nums: [int]) -> int:
        n = max(max(nums), len(nums))

        for num in sorted(nums, reverse=True):
            if(num != n):
                return n
            n -= 1
        return 0