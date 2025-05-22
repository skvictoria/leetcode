# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, value):
        if not root:
            return value
        self.inorder(root.left, value)
        value.append(root.val)
        self.inorder(root.right, value)
        return value

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        value = []  
        value = self.inorder(root, value)
        diff = []
        first = value[0]
        for i in range(1, len(value)):
            diff.append(value[i] - first)
            first = value[i]
        return min(diff)
        