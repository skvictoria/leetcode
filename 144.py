# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        stack = []
        curr = root
        output = []
        
        while curr or stack:
            if curr:
                output.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                curr = curr.left

            else:
                curr = stack.pop()
        return output

