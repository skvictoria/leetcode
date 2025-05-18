# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        res = []
        memory = [(root, str(root.val))]
        while memory:
            node, path = memory.pop()
            if node.left is None and node.right is None:
                res.append(path)
            if node.right:
                memory.append((node.right, path+"->"+str(node.right.val)))
            if node.left:
                memory.append((node.left, path+"->"+str(node.left.val)))
        return res

