class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        i = len(nums)-1
        res = nums[:]
        while(left <= right):
            if nums[left]*nums[left] < nums[right]*nums[right]:
                res[i] = nums[right]*nums[right]
                right -= 1
                i -= 1
            else:
                res[i] = nums[left]*nums[left]
                i -= 1
                left += 1
        return res
        