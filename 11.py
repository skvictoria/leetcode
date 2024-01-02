'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''
import numpy as np
class Solution:
    def maxArea_bruteforce(self, height: List[int]) -> int:
        dp = np.zeros(len(height))
        for i in range(len(height)):
            max = 0
            for j in range(0, i):
                temp_wide = (i-j) * min(height[i], height[j])
                if(max < temp_wide):
                    max = temp_wide
            dp[i] = max
        return int(np.max(dp))
    
    def maxArea_twopointer(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        while(right>left):
            current_area = min(height[right], height[left]) * (right-left)
            max_area = max(current_area, max_area)

            if(height[left] < height[right]):
                left += 1
            else:
                right -=1
        return max_area