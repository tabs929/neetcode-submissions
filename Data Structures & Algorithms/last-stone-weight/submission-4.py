class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-s for s in stones]
        heapq.heapify(heap)

        while len(heap)>1:
            a,b=-heapq.heappop(heap),-heapq.heappop(heap)
            if a>b:
                heapq.heappush(heap,-(a-b))
            elif a==b:
                #heapq.heappush(heap,-(b-a))
                continue
                
        return -heap[0] if heap else 0