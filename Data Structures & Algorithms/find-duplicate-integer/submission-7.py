class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # implement floyds algorithm
        # basically keep walking slow and fast pointer
        # the first time they meet is recorded as the start of the cycle
        # then you walk from 0 on a poointer and from the first meeting
        # first time they meet is the duplicate element
        # this was proven mathematically already that they will be of the same distance from the repeated element

        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break;

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if(slow == slow2):
                return slow