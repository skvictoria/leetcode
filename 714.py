'''
0
3-1-2
3-1-2


'''

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) == 1:
            return 0
        profit = [0] * len(prices)

        profit[0] = 0
        profit[1] = max(prices[1] - prices[0] - fee, 0)
        for i in range(1, len(prices)):
            profit[i] = 

