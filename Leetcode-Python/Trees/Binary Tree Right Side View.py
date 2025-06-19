from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        
        res = []
        q = deque([root])

        # Remember is VISIBLE from the right. So you just need to go to the last node
        # of each level and append it to your res.
        while q:
            initial_len = len(q)
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                if i == initial_len - 1:
                    res.append(node.val)
        
        return res