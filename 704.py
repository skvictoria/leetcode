'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        if(right == 0):
            if(target == nums[0]):
                return 0
            else:
                return -1
        while(right >= left):
            mid = (right+left)//2
            if((mid==right or mid==left) and nums[left]<target<nums[right]):
                return -1
            if(nums[mid] < target):
                left = mid+1
            elif(target < nums[mid]):
                right = mid-1
            else:
                return mid
        return -1
    
gg = Solution()
gg.search([-1, 0, 3, 5, 9, 12], 2)