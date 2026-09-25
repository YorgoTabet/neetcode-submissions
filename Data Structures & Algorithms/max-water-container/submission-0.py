class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxCap = 0
        l,r = 0, len(height)-1

        while(l<r):
            maxCap = max(maxCap, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
 
        return maxCap
        

# formula is delta * minHeight to get the amount of water 