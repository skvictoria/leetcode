class Solution:
    
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def dfs(index, currentXor):
            nonlocal res
            if len(nums) == index:
                res += currentXor
                return
            dfs(index + 1, currentXor)
            dfs(index + 1, currentXor ^ nums[index])
        dfs(0, 0)
        return res
