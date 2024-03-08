class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #1. input check
        res = 0
        if len(s) == 0:
            return 0
        #2.
        stack = []
        arr = [0]*len(s)
        
        for i, chr in enumerate(s):
            if chr == "(":
                stack.append(i)
            elif chr == ")":
                if len(stack) != 0:
                    arr[stack.pop()] = 1
                    arr[i] = 1
        consecutive = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                consecutive = 0
            else:
                consecutive += 1
                res = max(consecutive, res)
        return res