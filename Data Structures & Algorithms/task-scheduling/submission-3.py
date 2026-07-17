class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = Counter(tasks)

        heap = [-cnt for cnt in hm.values()]
        heapq.heapify(heap)

        q = deque()
        cycle = 0

        while heap or q:
            cycle+=1

            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([cnt,n+cycle])
            if q and q[0][1] == cycle:
                heapq.heappush(heap,q.popleft()[0])

        return cycle