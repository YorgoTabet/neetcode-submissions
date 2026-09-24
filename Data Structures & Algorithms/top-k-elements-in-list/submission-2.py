class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        map = defaultdict(int)
        bucket = [[] for i in range(len(nums) + 1)]
        

        for i in nums:
            map[i] += 1
        
        for n, c in map.items():
            bucket[c].append(n)


        for i in range(len(bucket) - 1, 0, -1):
            if(len(res) == k):
                break
            for n in bucket[i]:
                res.insert(0,n)

        
        return res
