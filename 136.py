'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

class Solution:
    def singleNumber(self, nums: [int]) -> int:
        ## Using XOR!
        single = 0
        for num in nums:
            single ^= num
        return single
    
        ## Using O(n^2).. not efficient
        # tempList = []
        # for number in nums:
        #     bflag = False
        #     for comp_num in tempList:
        #         if number == comp_num:
        #             tempList.remove(comp_num)
        #             bflag = True
        #             break
        #     if(bflag == False):
        #         tempList.append(number)
        # return tempList[0]

res = Solution()
res.singleNumber([4,1,2,1,2])