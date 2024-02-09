from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root == None):
            return []
        queue = deque([root])
        res = []
        while queue:
            tmp = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                tmp.append(node.val)
                if(node.left != None):
                    
                    queue.append(node.left)
                if(node.right != None):
                    
                    queue.append(node.right)
            res.append(tmp)
        return res