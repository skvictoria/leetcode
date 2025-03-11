class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum_list = [0]
        temp_sum = 0
        for arg in gain:
            temp_sum += arg
            sum_list.append(temp_sum)
        return max(sum_list)