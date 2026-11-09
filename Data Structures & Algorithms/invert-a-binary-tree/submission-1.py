# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # DEPTH FIRST SEARCH SOLUTION
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if current node is not a root (no children)
        # we have reached the final node
        if not root:
            return None
        
        # Shorthand instead of storing a temp
        root.left, root.right = root.right, root.left

        #Recursively call the function on the current left and right nodes
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
