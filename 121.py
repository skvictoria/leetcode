'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        min = 100001
        max = -1
        
        for idx in range(len(prices)):
            # only if found minimum
            if(min > prices[idx]):
                min = prices[idx]
            if(max < prices[idx] - min):
                max = prices[idx] - min
                
        
        if(min ==100001 or max < 0):
            return 0
        return max
add = Solution()
add.maxProfit([3,3,5,0,0,3,1,4])