# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # RECURSIVE DEPTH FIRST SEARCH
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # otherwise there is a root node so return 1 + (left, right)
        # if there are no children, the base case fires and returns 0
        # so max(0, 0) will be 0 and return 1 for the root depth
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
