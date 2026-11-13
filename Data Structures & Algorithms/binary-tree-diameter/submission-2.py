# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Space Complexity:
        O(n)

        Time Complexity:
        O(n) for non balanced tree
        O(log n) for balanced tree
        """
        # Set a global starting point of 0
        res = 0
        # Also can set as member variable:
        # self.res = 0
        # -> Need to then use self.res below and remove nonlocal

        def dfs(root):
            # specifies that res is in the outer scope
            nonlocal res

            # nothing
            if not root:
                return 0
            # recursively call dfs on the each child
            # and store in variable
            left = dfs(root.left)
            right = dfs(root.right)
            # set the outer scope result to the max between current res
            # and left + right
            # l + r 
            # In the case that  1
            #                  / \
            #                 2   3
            # the left and right will be called and will be root
            # then another recursive call on each will return 0
            # this will set res = max(0, 0 + 0)
            # which bubbles up to the first call to also return 0's
            # but the return will return the left and right as 1, 1
            # so then in the last recursion
            # the function will have set res=2
            # and it will return the height 1 + max(1,1) = 2

            res = max(res, left + right)
            print(res)
            return 1 + max(left, right)
        
        asd = dfs(root)
        dfs(root)
        print("both:",asd, res)
        # return res, not what the function returns because that is the height
        # not the diameter
        return res