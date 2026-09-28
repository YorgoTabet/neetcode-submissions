class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            currentTotal = numbers[l] + numbers[r]
            if currentTotal == target:
                return [l + 1, r + 1]
            elif currentTotal > target:
                r-=1
            else:
                l+=1

        return []
