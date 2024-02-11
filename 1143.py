class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        
        df = [0] * (len(text1)+1)
        for i in range(1, len(text2)+1):
            prev = 0
            for j in range(1,len(text1)+1):
                temp = df[j]
                if(text1[j-1] == text2[i-1]):
                    df[j] = prev+1
                else:
                    df[j] = max(df[j-1], df[j])
                prev = temp
        return df[len(text1)]
        
sol = Solution()
print(sol.longestCommonSubsequence("bsbininm", "jmjkbkjkv"))