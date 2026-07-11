class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preRec = defaultdict(list)

        for crs,preq in prerequisites:
            preRec[crs].append(preq)
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for preq in preRec[crs]:
                if not dfs(preq):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            op.append(crs)
            return True

        op=[]
        visited,cycle = set(),set()
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return op