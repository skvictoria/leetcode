class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            # Select ith number
            select = nums[i]
            # Find if target - nums[i] is there.
            for j in range(i+1, len(nums)):
                
                # if Found, return
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    return res
                # else, loop through again