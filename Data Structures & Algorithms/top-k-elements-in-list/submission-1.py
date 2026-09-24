class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        map = defaultdict(int)
        heap = []

        for i in nums:
            map[i] += 1
        
        for key in map.keys():
            heapq.heappush(heap, (-(map[key]), key))
        
        for i in range(k):
            c = heapq.heappop(heap)
            res.append(c[1])
        
        return res