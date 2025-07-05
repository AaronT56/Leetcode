from collections import deque
# Both DFS and BFS can be used. I show both.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = deque()
        q.append((root, root.val))
        goodnodes = 0
        newmax = float("-inf")

        while q:
            # I keep the i in range.. line but it's actually unnecessary unless you are
            # going row by row but im just iterating through the tree so this is not
            # needed at all.
            for i in range(len(q)):
                # The key to remember here that I didn't realise, is that each node has
                # it's own individual max and that max will only be assigned to other nodes
                # further down in its tree. So we don't need to separate our maxes, they
                # are separated by default due to how the code works. Look here:
                node, currmax = q.popleft()
                if currmax <= node.val:
                    goodnodes += 1

                newmax = max(currmax, node.val) # Note newmax is CURRMAX and node.val. This
                # keeps the node maxs independent so each time you are popping the current
                # nodes value and the max of all values previous.

                # So we are essentially passing on the max from the previous node, 
                # and giving it to the next node. Hence the max is maintained along
                # the chain and is individual to each node (associated with value in
                # the queue)
                if node.left:
                    q.append((node.left, newmax))

                if node.right:
                    q.append((node.right, newmax))
                
        return goodnodes
    

    def goodNodesBFS(self, root: TreeNode) -> int:
        # This is a pretty cool clean solution actually. Kinda less clunky than the other
        def dfs(node, maxval):
            if not node:
                return 0
            
            res = 1 if maxval <= node.val else 0
            maxval = max(maxval, node.val)
            res += dfs(node.left, maxval)
            res += dfs(node.right, maxval)
            return res
        res = dfs(root, root.val)
        return res
        
