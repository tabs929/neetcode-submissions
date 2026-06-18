from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerec = defaultdict(list)
        for c,p in prerequisites:
            prerec[c].append(p)

        def cycle(c,seen):
            if c in seen:
                return True
            seen.add(c)
            for p in prerec[c]:
                if cycle(p,seen):
                    return True
            prerec[c] = []
            seen.remove(c)
            return False


        seen = set()
        for course in range(numCourses):
            if cycle(course,seen):
                return False
        return True