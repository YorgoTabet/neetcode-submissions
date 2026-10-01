# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        map = {}

        tail = head
        while(tail.next):
            map[tail.next] = tail
            tail = tail.next
            
        while(head and head.next and head.next is not tail):
            tail.next = head.next
            head.next = tail

            tail = map.get(tail)
            tail.next = None
            head = head.next and head.next.next
        

            
        