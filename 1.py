class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force example
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


        # two-pass hash table
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            if (target - nums[i]) in hashmap and hashmap[target-nums[i]] != i:
                return i, hashmap[target-nums[i]]