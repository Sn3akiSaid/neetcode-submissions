# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Nothing, return True
        if not p and not q:
            return True
        # Something, and both vals at this position are equal
        # Do not return true but instead enter a recursive loop that returns both
        # trees comparing the lefts and the rights
        if p and q and p.val == q.val:
            # Here the and ensures both sides get tested but ALSO that they both return
            # True for the final result to be True
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # Something else
        # 2 == 3 or 4 == null 
        else:
            return False