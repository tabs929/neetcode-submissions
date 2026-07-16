class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-s for s in stones]
        heapq.heapify(heap)

        while len(heap)>1:
            a,b=heapq.heappop(heap),heapq.heappop(heap)
            if b>a:
                heapq.heappush(heap,a-b)
        
        heap.append(0)
        return -heap[0]