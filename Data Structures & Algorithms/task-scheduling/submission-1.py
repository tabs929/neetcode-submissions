from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = Counter(tasks)

        heap = [-c for c in hm.values()]
        heapq.heapify(heap)

        time = 0
        q = deque()

        while heap or q:
            time += 1

            if heap:
                cnt = 1 + heapq.heappop(heap)

                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time