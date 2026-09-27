class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prod = 1

        # prefix run
        for i in range(len(nums)):
            res[i] *= prod
            prod *= nums[i]


        prod = 1
        for i in reversed(range(len(nums))):
            res[i] *= prod
            prod*=nums[i]

        return res