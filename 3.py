class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        start = 0
        max_start = 0
        max_length = 0
        for end in range(len(s)):
            # if found the same one in the hashmap
            if(s[end] in char_index_map and char_index_map[s[end]] >= start):
                # update the start
                start = char_index_map[s[end]] + 1
            # store in the hashmap
            char_index_map[s[end]] = end
            
            # if the end - start + 1 > max_length
            if(end - start + 1 > max_length):
                # update the max_length
                max_length = end - start + 1
                # update the max_start
                max_start = start
        return max_length
    
