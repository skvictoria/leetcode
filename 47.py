class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        return self.helper(0, nums)
    
    def helper(self, index, nums):
        if index == len(nums):
            return [[]]
        res = []
        perms = self.helper(index+1, nums)
        for perm in perms:
            for j in range(len(perm) + 1):
                if j!=0 and perm[j-1] == nums[index]:
                    break
                prev = j
                permc = perm.copy()
                permc.insert(j, nums[index])
                res.append(permc)
        return res