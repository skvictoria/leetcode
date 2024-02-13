class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        res = [[1], [1,1]]
        
        for i in range(3, numRows+1):
            tmp = []
            tmp.append(1)
            for j in range(len(res[-1]) - 1):
                tmp.append(res[-1][j] + res[-1][j+1])
            tmp.append(1)
            res.append(tmp)
        
        return res
        