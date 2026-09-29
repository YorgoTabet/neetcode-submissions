class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0] * len(temperatures)
        stack = []

        for index, val in enumerate(temperatures):
            while(len(stack) and temperatures[stack[-1]] < val):
                targetIndex = stack.pop()
                arr[targetIndex] = index - targetIndex
            stack.append(index)

        return arr
