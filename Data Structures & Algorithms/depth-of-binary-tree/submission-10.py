# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # ITERATIVE DFS NOTES
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
            
        queue = deque([root])
        lvl = 0
        # why is this breadth?
        #    1
        #   2  3
        #       4
        # 3 different levels for this case 
        # [1] - > [2,3] - > [4]
        # while there is a queue, we want FOR each node within a level
        # to remove the first node we see and check it for kids
        # if there are kids push them to queue
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Once we check each node of the level
            # break out of loop and progress the level
            lvl += 1
        return lvl