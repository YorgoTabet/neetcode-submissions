# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        count = 0
        initial = head
        dummy = ListNode()
        
        # one pass to figure out how many parts you should flip
        while head:
            head = head.next
            count +=1

        head = initial
        prev = None
        prevTail = dummy
        for i in range((count // k)):
            newTail = head
            for i in range(k):
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            prevTail.next = prev
            prev = None
            prevTail = newTail

        
        prevTail.next = head

        return dummy.next
                