class Solution:
    def numberOfSteps(self, num: int) -> int:
        remain = num
        idx = 0
        while remain is not 0:
            if remain % 2 == 0: # even
                remain = remain // 2
            else:
                remain = remain - 1
            idx += 1
        return idx