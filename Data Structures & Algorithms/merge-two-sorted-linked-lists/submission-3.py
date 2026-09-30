# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        initial = list1 if list1.val <= list2.val else list2

        while list1 and list2:
            print(list1.val, list2.val)
           # if list1.val is smaller check the two next options
            if list1.val <= list2.val:
                hold = list1.next
                if(hold and hold.val <= list2.val):
                    list1 = list1.next
                else:
                    list1.next = list2
                    list1 = hold
           # if list2.val is smaller check the two next options
            else:
                hold = list2.next
                if(hold and hold.val < list1.val):
                    list2 = list2.next
                else:
                    list2.next = list1
                    list2 = hold

        return initial
        