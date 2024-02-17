# algorithm: dp
# Big O: O(n^2)
# data structure: set 

class Solution:   
    def wordBreak(self,s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] is True and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[len(s)]