# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])
        root_id = len(nums) // 2
        
        ret = TreeNode(val=nums[root_id])
        ret.left = self.sortedArrayToBST(nums[:root_id])
        if root_id + 1 < len(nums):
            ret.right = self.sortedArrayToBST(nums[root_id+1:])
        return ret