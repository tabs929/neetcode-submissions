class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        hm = Counter(hand)
        heap = list(hm.keys())
        heapq.heapify(heap)

        while heap:
            n = heap[0]
            for i in range(n, n + groupSize):
                if i not in hm:
                    return False
                hm[i]-=1
                if hm[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
        return True
        