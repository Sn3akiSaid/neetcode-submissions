# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # There are children
        if root.left or root.right:
            # return 1 + the max depth of each subtree
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        # No children
        else:
            # return only the current node
            return 1
        
