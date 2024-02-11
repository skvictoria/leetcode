class Solution:
    def heapify(self, unsorted, index, n):
        left = index *2 + 1
        right = index *2 + 2
        minimum_index = index

        if left < n and unsorted[minimum_index] < unsorted[left]:
            minimum_index = left
        if right < n and unsorted[minimum_index] < unsorted[right]:
            minimum_index = right
        
        if minimum_index != index:
            unsorted[minimum_index], unsorted[index] = unsorted[index], unsorted[minimum_index]
            self.heapify(unsorted, minimum_index, n)

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        res = []
        for i in range(n//2-1, -1, -1):
            self.heapify(nums, i, n)
        
        for i in range(n-1, 0, -1):
            res.append(nums[0])
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, 0, i)
        nums = res