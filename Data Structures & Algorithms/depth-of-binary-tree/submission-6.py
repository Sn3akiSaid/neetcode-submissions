# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # ITERATIVE DEPTH FIRST SEARCH 
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # No need to check for null if res starts at 0
        # Root gets popped in while loop and there is no node
        stack = [[root , 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            # Non Null node
            if node:
                res = max(res, depth)
                # Might add null nodes here because the children could be node
                # This however gets popped above, and we do nothing with it

                # Append from left and increase the depth
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res