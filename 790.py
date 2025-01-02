class Solution:
    def numTilings(self, n: int) -> int:
        # n=1: 1 (1)
        # n=2: 2 (11, 2)
        # n=3: 5 (111, 12, 21, 3)
        # n=4: (1111, 112, 121, 211, 13, 31, 22)
        arr = [''] * n
        arr[0] = 1
        if n == 1:
            return arr[0]
        arr[1] = 2
        if n == 2:
            return arr[1]
        arr[2] = 5
        for i in range(3, n):
            arr[i] = (2 * arr[i-1] + arr[i-3]) % (10**9 + 7)
        return arr[-1]