class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            minus = True
            x = -x
        else:
            minus = False
        
        y = 0
        while True:
            remain = x % 10 # 123/10 = 12, 3   12/10 = 1,2   1/10=0,1
            if x is 0 and remain is 0:
                break
            y = y * 10
            y += remain
            x = x // 10
            if y >= (2**31) - 1:
                return 0
        if minus == True:
            y = -y
        return y