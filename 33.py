class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while L <= R:
            M = (L+R)//2
            if nums[L] <= nums[M]:
                if nums[L] < target < nums[M]:
                    R = M
                elif target == nums[L]:
                    return L
                elif target == nums[M]:
                    return M
                else:
                    L = M+1
            else:
                if nums[M] < target < nums[R]:
                    L = M
                elif target == nums[M]:
                    return M
                elif target == nums[R]:
                    return R
                else:
                    R = M-1
        return -1
