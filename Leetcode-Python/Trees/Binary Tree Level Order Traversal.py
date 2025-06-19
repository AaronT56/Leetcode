from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            level = []
            # This is a nifty trick. Checks the length of q right now and only goes 
            # through the queue till that point. Really good for bfs going down the
            # levels.
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)
        return res
