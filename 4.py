class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_list = nums1 + nums2
        merge_list = sorted(merge_list)
        if len(merge_list) % 2 == 1:
            return merge_list[int(len(merge_list)/2)]
        else:
            return (merge_list[int(len(merge_list)/2) -1] + merge_list[int(len(merge_list)/2)])/2