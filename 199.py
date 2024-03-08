from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ret = []
        qu = deque()
        qu.append(root)
        while qu:
            length = len(qu)
            for i in range(length):
                leftnode = qu.popleft()
                if i == length - 1:
                    ret.append(leftnode.val)

                if leftnode.left:
                    qu.append(leftnode.left)
                if leftnode.right:
                    qu.append(leftnode.right)
        return ret