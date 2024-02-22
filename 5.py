'''
Algorithm
: two pointer

left = 0
right = len(s)-1
for left in range(len(s)):
    for right in range(len(s)-1, left):
        if s[left] == s[right]:
            candidate_left = s[left]
            candidate_right = s[right]
            while left < right:
                left += 1
                right -= 1
                if left != right:
                    candidate_left = ''
                    candidate_right = ''
                    break
                else:
                    candidate_left += s[left]
                    candidate_right += s[right]
            if candidate_left and candidate right is not None:
                return candidate_left + candidate_right.reverse()

return ""

O(n^3) in worst case?
'''

class Solution:
    def center(self, left, right, s):
        
        while(right <= len(s)-1 and left >= 0):
            if(s[left] == s[right]):
                
                left -= 1
                right += 1
            else:
                break
        return right - left - 1
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_left = 0
        for i in range(len(s)):
            len1 = self.center(i, i, s)
            len2 = self.center(i, i+1, s)
            if max_len < max(len1, len2):
                max_len = max(len1, len2)
                max_left = i
                max_right = i if len1>len2 else i+1
        return s[max_left-(max_len-1)//2:max_left-(max_len-1)//2+max_len]
    # def longestPalindrome(self, s: str) -> str:
    #     candidate = []
    #     # iterate through s
    #     for left in range(len(s)):
    #         right = len(s)-1
    #         while(right >= left):
    #             # if left == right,
    #             if s[left] == s[right]:
    #                 # it is a candidate
    #                 candidate_left = ""
    #                 candidate_right = ""
    #                 cand_left = left
    #                 cand_right = right
    #                 while cand_left <= cand_right:
    #                     if s[cand_left] != s[cand_right]:
    #                         candidate_left = ""
    #                         candidate_right = ""
    #                         break
    #                     elif cand_left == cand_right:
    #                         candidate_left += s[cand_left]
    #                     else:
    #                         candidate_left += s[cand_left]
    #                         candidate_right += s[cand_right]
    #                     cand_left += 1
    #                     cand_right -= 1
    #                 if candidate_left is not "" or candidate_right is not "":
    #                     candidate.append(candidate_left + candidate_right[::-1])
    #             right -= 1
    #     max_len = 0
    #     max_id = 0
    #     for i in range(len(candidate)):
    #         if max_len < len(candidate[i]):
    #             max_len = len(candidate[i])
    #             max_id = i
    #     return candidate[max_id]