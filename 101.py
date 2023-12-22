# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def MirrorCheck(self, root1, root2):
        bResult = True
        if(root1 == None and root2 == None):
            return True
        elif(root1 == None):
            return False
        elif(root2 == None):
            return False
        # root1, root2 value check
        if(root1.val != root2.val):
            bResult = False
            return bResult
        # root1.left / root2.right value check
        if(self.MirrorCheck(root1.left, root2.right) == False):
            bResult = False
            return bResult
        # root1.right / root2.left value check
        if(self.MirrorCheck(root1.right, root2.left) == False):
            bResult = False
            return bResult
        return bResult
    
    def isSymmetric(self, root: [TreeNode]) -> bool:
        bResult = True
        # Base Case
        if(self.MirrorCheck(root.left, root.right) == False):
            bResult = False
                
        return bResult