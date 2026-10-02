class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("+inf")
        maxProf = 0

        for i in prices:
            minPrice = min(minPrice, i)
            maxProf = max(maxProf, i - minPrice)
        
        return maxProf