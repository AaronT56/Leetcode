class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # The idea is to go as far left in the stack as possible
        # pop from the stack and only go right when we need to.
        # One important insight is that once you go past a node
        # in a tree on the left, all nodes after that MUST be less
        # than that node. So this order works out well. 

        res = None
        count = 0
        def dfs(node):
            nonlocal res, count
            if not node:
                return
            
            dfs(node.left)

            count += 1

            if count == k:
                res = node.val
                return
            
            dfs(node.right)
        
        dfs(root)
        return res
                
