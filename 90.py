class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets, curset = [], []
        nums_sorted = sorted(nums)
        self.helper(0, nums_sorted, subsets, curset)
        return subsets
    
    def helper(self, i, num, subsets, curset):
        if i >= len(num):
            subsets.append(curset.copy())
            return

        # add one
        curset.append(num[i])
        self.helper(i+1, num, subsets, curset)
        curset.pop()

        # not adding
        while (i+1) < len(num) and num[i] == num[i+1]:
            i += 1
        self.helper(i+1, num, subsets, curset)