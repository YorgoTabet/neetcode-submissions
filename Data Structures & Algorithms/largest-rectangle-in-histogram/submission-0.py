class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0

        nextSmaller = [len(heights)] * len(heights)

        stack = []

        for i in range(len(heights)):
            while len(stack) and heights[stack[-1]] > heights[i]:
                biggerHeightIdx = stack.pop()
                nextSmaller[biggerHeightIdx] = i
            stack.append(i)

        stack = []
        previousSmaller = [-1] * len(heights)

        for i in range(len(heights) - 1, -1, -1):
            while len(stack) and heights[stack[-1]] > heights[i]:
                biggerHeightIdx = stack.pop()
                previousSmaller[biggerHeightIdx] = i
            stack.append(i)

        for i in range(len(heights)):
            width = nextSmaller[i] - previousSmaller[i] - 1
            res = max(res, width * heights[i])

        return res


"""
1, 4, 3, 4, 1

maxArea = 7
minHeight = 2

formula is (i1 -i2 + 1) * minHeight

track maximum area
if decreasing dont add the outer bound
if height increase update bound

"""
