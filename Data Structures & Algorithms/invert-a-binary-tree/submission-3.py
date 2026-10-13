# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None

        queue = deque([root])
        while queue:
            current = queue.pop()
            current.left, current.right = current.right, current.left
            if current.left:
                queue.appendleft(current.left)
            if current.right:
                queue.appendleft(current.right)

        return root