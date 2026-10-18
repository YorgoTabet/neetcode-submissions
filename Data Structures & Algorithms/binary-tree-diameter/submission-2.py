# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def max_h(root):
            if not root:
                return 0
            left = max_h(root.left)
            right = max_h(root.right)

            self.res = max(left + right, self.res)

            return 1 + max(left, right)

        max_h(root)
        return self.res
            
