from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        for c,p in prerequisites:
            pre[c].append(p)

        def cycle(c,seen):
            if c in seen:
                return True
            seen.add(c)
            for p in pre[c]:
                if cycle(p,seen):
                    return True
            pre[c] = []
            seen.remove(c)
            return False


        seen = set()
        for c in range(numCourses):
            if cycle(c,seen):
                return False
        
        return True