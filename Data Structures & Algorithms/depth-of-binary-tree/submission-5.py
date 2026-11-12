# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # ITERATIVE BREADTH FIRST SEARCH
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        # Initially only root in deck queue
        queue = deque([root])
        count = 0
        # while queue not empty
        while queue:
            # for every element in queue at this current time
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            count += 1
            
        return count