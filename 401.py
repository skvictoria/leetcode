class Solution:
    def countOnes(self, n):
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n = n // 2
        return count

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        flag = 0
        res = []
        for i in range(0, 12):
            if turnedOn >= self.countOnes(i):
                for j in range(0, 60):
                    if turnedOn == self.countOnes(i) + self.countOnes(j):
                        res.append(str(i)+":"+str(j).zfill(2))
                        
        return res