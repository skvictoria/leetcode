class Solution:
    def dp(self, i, j):
        if i == self.len1:
            return self.len2 - j
        if j == self.len2:
            return self.len1 - i

        if (i,j) in self.cache:
            return self.cache[(i,j)]
        
        if self.word1[i] == self.word2[j]:
            self.cache[(i,j)] = self.dp(i+1, j+1)
        else:
            temp = min(self.dp(i+1, j), self.dp(i+1, j+1))
            self.cache[(i,j)] = min(temp, self.dp(i, j+1)) + 1
        return self.cache[(i,j)]

    def minDistance(self, word1: str, word2: str) -> int:
        self.word1 = word1
        self.word2 = word2
        self.len1 = len(word1)
        self.len2 = len(word2)
        self.cache = {}

        return self.dp(0,0)