# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node, depth):
        if node.left is None and node.right is None:
            return depth
        elif node.left is not None and node.right is not None:
            depth += 1
            return max(self.dfs(node.left, depth), self.dfs(node.right, depth))
        elif node.left is not None:
            depth += 1
            return self.dfs(node.left, depth)
        else:
            depth += 1
            return self.dfs(node.right, depth)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 1
        return self.dfs(root, depth)
            