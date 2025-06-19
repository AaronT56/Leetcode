from typing import Optional
class TreeNode:
    def __init__(self, val = 0, left = None, Right = None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            self.res = max(self.res, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return self.res