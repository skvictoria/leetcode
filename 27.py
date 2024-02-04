class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        sorted_nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if(val != nums[i]):
                res.append(nums[i])
        nums[:len(res)] = res
        return len(res)
    
gg = Solution()
print(gg.removeElement([3,2,2,3], 3))