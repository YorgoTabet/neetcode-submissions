# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class FlaggedListNode(ListNode):
    checked = False

    def __init__(self, val=0, next=None, checked=False):
        super().__init__(val, next)
        self.checked = checked


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        map = {}
        while head:
            map[head] = True

            if not head.next:
                return False
            elif map.get(head.next):
                return True
            else:
                head = head.next
