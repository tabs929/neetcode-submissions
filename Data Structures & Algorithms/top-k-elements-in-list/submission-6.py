class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        hm = Counter(nums)
        res = []
        
        for num,cnt in hm.items():
            heapq.heappush(minHeap,[cnt,num])
            if len(minHeap)>k:
                heapq.heappop(minHeap)

        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res