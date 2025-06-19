class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        # These work kind of like backtracking. Where we call over and over until
        # we reach the bottom of the tree from left side. Then adjust all the pointers
        # going back upwards until we finally reach the top and have root now with 
        # inverted pointers.
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    