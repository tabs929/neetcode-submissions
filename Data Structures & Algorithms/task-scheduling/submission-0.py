class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = Counter(tasks)
        heap = [-c for c in hm.values()]
        heapq.heapify(heap)
        cycle = 0
        q = deque()

        while q or heap:
            cycle+=1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([cnt,cycle+n])

            if q and q[0][1] == cycle:
                heapq.heappush(heap,q.popleft()[0])
        return cycle