# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        initial = head
        count = 0

        while head:
            count += 1
            head = head.next

        dummy = ListNode(0, initial)
        current = dummy

        for i in range(-1, count):
            if i + 1 == (count - 1) - (n - 1) and current.next:
                current.next = current.next.next
            current = current and current.next or None

        return dummy.next


