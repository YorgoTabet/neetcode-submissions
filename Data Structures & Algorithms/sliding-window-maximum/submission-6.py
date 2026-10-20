class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []

        
        for r in range(len(nums)):
            l = r - k + 1
            right = nums[r]
            left = nums[l]
    
            heapq.heappush(heap, (-right, r))
            if l >= 0:   
                res.append(-heap[0][0])

                while(l >= 0 and len(heap) and heap[0][1] <= l):
                    heapq.heappop(heap)
   

        return res
