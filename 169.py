class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        sorted_nums = sorted(nums)
        cnt = 1
        prev = sorted_nums[0]
        for i in range(1,len(sorted_nums)):
            if sorted_nums[i] == prev:
                cnt += 1
                if cnt > int(n/2):
                    return sorted_nums[i]
            else:
                prev = sorted_nums[i]
                cnt = 1
        return sorted_nums[-1]