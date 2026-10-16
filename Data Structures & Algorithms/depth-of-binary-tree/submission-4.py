from collections import deque

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
        # depth first traversal
        queue = [root]
        level = 0
        while len(queue):
            newqueue = []
            while len(queue):
                node = queue.pop(0)
                if node:
                    newqueue.append(node.left)
                    newqueue.append(node.right)
            queue = newqueue
            level += 1 if len(newqueue) else 0
        return level





