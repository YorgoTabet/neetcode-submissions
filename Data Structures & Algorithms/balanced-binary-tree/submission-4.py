# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    unbalanced = False
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def getHeight(root):
            if not root:
                return 0
            left_height = getHeight(root.left)
            right_height = getHeight(root.right)
            if abs(left_height - right_height) > 1:
                self.unbalanced = True
            return 1 + max(right_height, left_height)

        getHeight(root)

        return not self.unbalanced