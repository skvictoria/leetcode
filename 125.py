class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ''.join(c for c in s if c.isalnum())
        
        left = 0
        right = len(c) - 1
        for i in range(len(c)):
            if c[left].lower() == c[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True