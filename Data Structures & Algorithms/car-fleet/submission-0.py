class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        sortedWithSpeed = [(p, speed[index]) for index, p in enumerate(position)]
        sortedWithSpeed.sort(key=lambda x: x[0])

        while(len(sortedWithSpeed)):
            current = sortedWithSpeed.pop()
            currentP = current[0]
            currentS = current[1]

            arrivesAfter = (target - currentP) / currentS

            while(
                len(sortedWithSpeed)
                and ((target - sortedWithSpeed[-1][0]) / sortedWithSpeed[-1][1])
                <= arrivesAfter
                ):

                sortedWithSpeed.pop()
            res+=1

        return res


"""
4, 1, 0, 7

(0, 2), (1, 2),(4,2), (7, 1), 10

# get the number of steps for last element
(target - position ) / speed
10 - 7 / 1 = 3
# while numbers after reach the destination pop them

10 - 4 / 2 = 1
"""