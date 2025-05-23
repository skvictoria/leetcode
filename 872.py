# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaf(self, root, leaflist):
        if not root.left and not root.right:
            leaflist.append(root.val)
            return leaflist
        if root.left:
            leaflist = self.findLeaf(root.left, leaflist)
        if root.right:
            leaflist = self.findLeaf(root.right, leaflist)
        return leaflist
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_list = []
        root2_list = []
        root1_list = self.findLeaf(root1, root1_list)
        root2_list = self.findLeaf(root2, root2_list)
        if root1_list == root2_list:
            return True
        else:
            return False