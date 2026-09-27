class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check if you're at the start
        # if you're not  continue
        # if you are, keep adding to the set until you don't have the next
        # store max 
        numSet = set(nums)
        res = 0

        for num in nums:
            length = 1

            if(num - 1 not in numSet):
                while(num + length in numSet):
                    length+=1
                    
            res = max(length, res)
                    

        return res



# visualization
# 2, 20, 4, 10, 3, 4, 5
#
# 2,3,4,5    10          20