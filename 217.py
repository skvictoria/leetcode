class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sets = set(nums)
        sets = list(sets)
        if(len(sets) != len(nums)):
            return True
        else:
            return False