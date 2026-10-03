class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r= len(nums) - 1

        while(l <= r):
            m = l + ((r - l) // 2)
            print(m)
            if(target == nums[m]):
                return m
            if(target < nums[m]):
                r = m - 1
            else:
                l = m + 1
        
        return -1
            
"""
0,5
5-0 //2 = 2 + 0
2 < 3, r = 2


4,5
1 + 4 = 5
2,5
5 - 2 = 3 //2  = 1 + 2 = 3

6 - 5 = 1// 2 = 0 + 5
"""