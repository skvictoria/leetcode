class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hashmap = set(nums1)
        nums2innums1 = 0
        for number in nums2:
            if number in hashmap:
                nums2innums1 += 1
        
        hashmap = set(nums2)
        nums1innums2 = 0
        for number in nums1:
            if number in hashmap:
                nums1innums2 += 1
        return ([nums1innums2, nums2innums1])
