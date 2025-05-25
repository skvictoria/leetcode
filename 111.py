# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDepth(self, root, depth, depthList):
        if root.left:
            self.findDepth(root.left, depth+1, depthList)
        if root.right:
            self.findDepth(root.right, depth+1, depthList)
        if not root.left and not root.right:
            depthList.append(depth)
        return

        
    # def minDepth(self, root: Optional[TreeNode]) -> int:
    #     if root is None:
    #         return 0
    #     depthList = []
    #     self.findDepth(root, 1, depthList)
    #     return min(depthList)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([(root, 1)])
        while root:
            root, depth = queue.popleft()
            if not root.left and not root.right:
                return depth
            if root.left:
                queue.append((root.left, depth+1))
            if root.right:
                queue.append((root.right, depth+1))