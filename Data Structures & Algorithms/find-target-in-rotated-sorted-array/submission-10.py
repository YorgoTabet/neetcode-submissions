class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we want to find in which part of the array our target exists
        # this happens by checking the l and r  and mid and deciding based on target where to move next

        l, r = 0, len(nums) - 1

        while(l<=r):
            mid = (l+r) // 2

            print(nums[l], nums[mid], nums[r], "target:", target)

            if(target == nums[mid]):
                return mid
            if(target < nums[mid]):
                if(target >= nums[l] or nums[r] >= nums[mid]):
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if(target <= nums[r] or nums[l] < nums[mid]):
                    l = mid + 1
                else:
                    r = mid -1

        return -1