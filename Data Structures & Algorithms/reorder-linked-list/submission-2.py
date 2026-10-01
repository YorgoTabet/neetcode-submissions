# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle of the linked list using slow, fast
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = prev = None

        # reverse second list
        while(second):
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
             

        # merge the two linked lists
        first, second = head, prev
        while(second and head):
            tmp1, tmp2 = first.next, second.next

            first.next = second 
            second.next = tmp1

            first = tmp1
            second = tmp2
        
        

        

            
        