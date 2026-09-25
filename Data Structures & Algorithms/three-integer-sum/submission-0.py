class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # store numbers and indices in sorted array (tuple with index)
        # start on the two furthest nnode and walk the middle pointer
        # if you find a 0 equality push it to res
        res = []
        nums.sort()

        def calculate(n1, n2, n3):
            return nums[n1] + nums[n2] + nums[n3]

        for i in range(len(nums)):
            target = nums[i]
            if(target > 0):
                return res
            if(i > 0 and target == nums[i - 1]):
                continue
            
            l = i + 1
            r = len(nums) - 1
            while(l < r):
                total = calculate(i,l,r)
                if(total == 0):
                    res.append([nums[i],nums[l],nums[r]])
                    r -= 1
                    l+=1
                    while(nums[l] == nums[l - 1] and l < r):
                        l+=1
                elif(total > 0):
                    r-=1
                else:
                    l +=1
        
        
        return res
        
                
