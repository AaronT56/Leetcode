from typing import Optional
class TreeNode:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left
    
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr:
                return [True, 0]
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]
        
        res = dfs(root)[0]

        return res
