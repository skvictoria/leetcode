class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        for i in range(len(accounts)):
            sum_temp = 0
            for j in range(len(accounts[i])):
                sum_temp += accounts[i][j]
            if sum_temp > max_sum:
                max_sum = sum_temp
        return max_sum