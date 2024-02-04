'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        vector_str_list = sorted(strs)
        min_length = min(len(strings) for strings in strs)
        res = ""

        for i in range(0, min_length):
            if vector_str_list[0][i] != vector_str_list[-1][i]:
                break
            res += vector_str_list[0][i]

        return res
        

gg = Solution()
gg.longestCommonPrefix(["ab", "a"])