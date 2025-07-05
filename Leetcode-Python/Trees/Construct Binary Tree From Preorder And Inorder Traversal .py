from typing import Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        

        # So the indexing works here because we want to skip the root each time and just
        # extract the separate trees. So in preorder, we skip first element and take up to 
        # to the midpoint. Whereas in inorder, we skip over the exact mid point (root) and
        # just include the left and right sides. That makes this pretty easy as we then 
        # just iterate through till we get the whole tree  figured out.
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
