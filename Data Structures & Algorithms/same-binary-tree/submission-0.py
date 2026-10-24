# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue = deque([p])
        q_queue = deque([q])
        self.same = True
        while len(p_queue) or len(q_queue):
            for index in range(len(p_queue)):
                q_node = q_queue.popleft()
                p_node = p_queue.popleft()
                if (p_node and p_node.val) != (q_node and q_node.val):
                    self.same = False
                    break
                if q_node:
                    q_queue.append(q_node.left)
                    q_queue.append(q_node.right)
                if q_node:
                    p_queue.append(p_node.left)
                    p_queue.append(p_node.right)
            

        return self.same
        