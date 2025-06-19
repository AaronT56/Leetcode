from typing import Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not subroot:
            return True
        
        if not root:
            return False
        
        if self.isSame(root, subroot):
            return True
        
        # So we have already established that root != subroot at this point. So we will
        # check further options. We find the next root.left and the next root.right that
        # we can find and see if those will work to give the subroot. If not, keep 
        # iterating in hopes of finding something that satisfies the above condition.
        
        return (self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot))
    def isSame(self, p : Optional[TreeNode], q : Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if p and q and q.val == p.val:
            return self.isSame(p.right, q.right) and self.isSame(p.left, q.left)
        
        return False