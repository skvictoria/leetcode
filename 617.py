# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        stack = [(root1, root2)]
        while stack:
            n1, n2 = stack.pop()
            if not n2:
                continue
            n1.val += n2.val

            if not n1.left:
                n1.left = n2.left
            else:
                stack.append((n1.left, n2.left))
            
            if not n1.right:
                n1.right = n2.right
            else:
                stack.append((n1.right, n2.right))
        return root1
        # if not root1:
        #     return root2
        # if not root2:
        #     return root1
        # q = deque([(root1, root2)])
        # while q:
        #     n1, n2 = q.popleft()
        #     if not n2:
        #         continue
        #     n1.val += n2.val

        #     if n2.left:
        #         if not n1.left:
        #             n1.left = n2.left
        #         else:
        #             q.append((n1.left, n2.left))
        #     if n2.right:
        #         if not n1.right:
        #             n1.right = n2.right
        #         else:
        #             q.append((n1.right, n2.right))
        # return root1
