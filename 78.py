class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]
        first = nums[0]
        nums.pop(0)
        sublist = self.subsets(nums)
        sublist2 = []
        for a in sublist:
            sublist2.append(a+[first])
        sublist2 += sublist
        return sublist2
