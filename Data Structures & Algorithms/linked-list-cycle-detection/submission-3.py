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
       # fast slow approach
        fast = head and head.next and head.next.next

        while fast:
            if fast is head:
                return True
            
            else:
                head = head.next
                fast = fast.next.next if fast.next else None
        
        return False
       
