'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 - n, 2 - 0 (45!/45! 0!) = 1
        # 1 - n-2, 2 - 1 (44!/43! 1!) = n-1/1!
        # 1 - n-4, 2 - 2 (43!/41! 2!) = n-2 n-3/2!
        # 1 - n-6, 2 - 3 (42!/39! 3!) = n-3 n-4 n-5 / 3!
        # 1 - n-8, 2 - 4 ()           = n-4 n-5 n-6 n-7 / 4!
        sum = 1
        for i in range(1, n):
            denom = 1
            num = 1
            for j in range (1, i+1):
                denom *= j
            for k in range (i, 2*i):
                num *= (n-k)
            sum += num/denom
        return int(sum)