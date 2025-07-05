from typing import Optional
class TreeNode:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            # This means both are terminating at the same time. This acts as base case to
            #  allow us to return back to earlier calls 
            # once we haven't encountered false and we eventually hit True, this true will
            #  just move back up the stack continuously. So basically if we hit that True
            #  condition without hitting a false, our trees are the same
            if not node1 and not node2:
                return True
            # This means one has terminated and the other hasn't (even though we
            # are propagating through the tree one step each time so they can't be
            # the same)
            if not node1 or not node2:
                return False
            # Must come after as otherwise node1 or node2 could be none which cause error
            if node1.val != node2.val:
                return False
            
            # If one of these calls returns false, then the whole tree will evaluate as
            # false. The recursive call is in the reutrn statement. So when a false is 
            # returned, all calls afterwards will also return false. Not we only
            # use the .left and .right here because that is all we are checking. At
            # each new node there will be a new unique left and right so we will check
            # all nodes and we are just following the same path in checking every node.
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
        
        return dfs(p, q)