# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        sumleft = 0
        while queue:
            node = queue.popleft()
            if node.left is not None and node.left.left is None and node.left.right is None:
                sumleft += node.left.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return sumleft