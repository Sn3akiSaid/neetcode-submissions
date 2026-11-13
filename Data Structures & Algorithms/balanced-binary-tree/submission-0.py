# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        This is identical to Diameter of Binary Tree
        Only that we look for height difference, not diameter

        (left + right) ---> abs(left - right)
        """
        self.diff = 0

        def height(root):
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            
            # Finds the maximum height difference at each call
            # Updates the local variable

            self.diff = max(self.diff, abs(left - right))
            
            # Returns the max height amongst the two child nodes
            return 1 + max(left, right)
        
        height(root)
        if self.diff > 1:
            return False
        return True