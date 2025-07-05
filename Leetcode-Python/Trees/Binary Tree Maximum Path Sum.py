from typing import Optional
class TreeNode:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left
    

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(curr):
            if not curr:
                return 0
            
            leftmax = dfs(curr.left)
            rightmax = dfs(curr.right)


            # We remove negatives, but even if the whole tree were negative we account for
            # this in the res calclation part.
            leftmax = max(leftmax, 0)
            rightmax = max(rightmax, 0)

            # Takes the values of both subtree's connected to curr, calcualtes their sum.
            # If this sum is greater than our previous res, make that shit res!
            res[0] = max(res[0], curr.val + leftmax + rightmax)

            return curr.val + max(leftmax, rightmax)
        
        dfs(root)

        return res