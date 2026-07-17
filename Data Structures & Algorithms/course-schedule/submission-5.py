class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preRec = defaultdict(list)

        for crs,preq in prerequisites:
            preRec[crs].append(preq)

        def dfs(crs):
            if crs in visited:
                return False
            if preRec[crs] == []:
                return True
            
            visited.add(crs)
            for preq in preRec[crs]:
                if not dfs(preq):
                    return False
            visited.remove(crs)
            preRec[crs] = []
            return True

        visited = set()
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True