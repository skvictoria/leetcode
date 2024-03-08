'''
idea
    if n == 0:
        return 1
    elif n < 0:
        n = -n
        for _ in n:
            ans *= x
        return 1/ans
    else:
        for _ in n:
            ans *= x
        return ans
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1/x
        
        if n % 2 == 0:
            ans = self.myPow(x, n//2)
            return ans*ans
        else:
            ans = self.myPow(x, n//2)
            return ans*ans*x