class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        sortedWithSpeed = [(p, s) for p,s in zip(position, speed)]
        sortedWithSpeed.sort()

        
        stack = []
        for p,s in sortedWithSpeed[::-1]:
            stack.append((target - p) / s)
            if(len(stack) >= 2 and stack[-1] <= stack[-2]):
                stack.pop()

        return len(stack)
        