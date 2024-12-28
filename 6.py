class Solution:
    def convert(self, s: str, numRows: int) -> str:
        output = s[0]
        for rowstartIdx in range(numRows):
            start = s[rowstartIdx]
            end = rowstartIdx
            while (end < 2*(numRows-rowstartIdx)):
                for j in range(rowstartIdx+1, numRows-1):
                    end += j * 2
                end += numRows - 1
                print(end)
                output += s[end]
        return output
        