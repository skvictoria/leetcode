class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        start = 0
        end = len(nums)-1

        if(start == end):
            if(nums[start] < target):
                return start+1
            else:
                return 0
            

        if(target < nums[start]):
            return 0
        if(nums[start]<target and target<nums[start+1]):
            return start+1
        if(nums[end-1]<target and target<nums[end]):
            return end
        if(nums[end]<target):
            return end+1

        while 1:
            tmp = int((start+end)/2)

            if(nums[tmp] > target):
                end = tmp
            elif(nums[tmp]<target):
                start = tmp
            else:
                return tmp

            if(nums[start] == target):
                return start
            elif(nums[end] == target):
                return end

            if(nums[start]<target and target<nums[start+1]):
                return start+1
            if(nums[end-1]<target and target<nums[end]):
                return end
            if(nums[end]<target):
                return end+1

        
Sol = Solution()
Sol.searchInsert([1],2)