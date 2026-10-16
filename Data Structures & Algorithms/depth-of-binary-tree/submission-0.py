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
        else:
            maxLeft = (root.left and self.maxDepth(root.left)) or 0
            maxRight = (root.right and self.maxDepth(root.right)) or 0
            return 1 + max(maxLeft, maxRight)