'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        for i in range(len(s)):
            for j in range(len(t)):
                if(s[i] == t[j]):
                    t = t.replace(s[i], '', 1)
                    break
        if(t != ''):
            return False
        else:
            return True
        
gg = Solution()
gg.isAnagram("anagram", "nagaram")