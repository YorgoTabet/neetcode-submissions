class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # get the total bananas/hours

        totalB = 0
        r = 0
        for pile in piles:
            totalB += pile
            r = max(r, pile)

        res = l = math.ceil(totalB / h)

        while l <= r:
            mid = math.floor(((r - l) / 2) + l)
            currentH = 0
            # count the total hours needed with midpoint
            for pile in piles:
                currentH += math.ceil(pile / mid)

            if currentH > h:
                l = mid + 1
            else:
                r = mid - 1
                res = mid


        return int(res)
