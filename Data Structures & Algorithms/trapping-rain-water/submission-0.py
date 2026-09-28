class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        # find max and store it
        mHeightIdx = 0
        for i, h in enumerate(height):
            if h > height[mHeightIdx]:
                mHeightIdx = i

        # walk in order until max
        l = 0
        r = 1
        while l < mHeightIdx:
            deducted = 0

            while r <= mHeightIdx and height[r] < height[l]:
                deducted += height[r]
                r += 1

            res += ((r - l - 1) * height[l]) - deducted
            l = r
            r += 1

        l = len(height) - 2
        r = len(height) - 1
        while r > mHeightIdx:
            deducted = 0

            while l >= mHeightIdx and height[l] < height[r]:
                deducted += height[l]
                l -= 1

            res += ((r - l - 1) * height[r]) - deducted
            r = l
            l -= 1

        return res
