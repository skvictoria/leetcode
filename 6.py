class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # initialization
        if numRows == 1:
            return s
        rows = [''] * numRows
        # trasversal
        curRow = 0
        down = True
        for char in s:
            rows[curRow] += char
            if down is True:
                if curRow == numRows - 1:
                    down = False
                    curRow -= 1
                else:
                    curRow += 1
            else: # down is False
                if curRow == 0:
                    down = True
                    curRow += 1
                else:
                    curRow -= 1
        output = ''
        for row in rows:
            output += row
        return output 
