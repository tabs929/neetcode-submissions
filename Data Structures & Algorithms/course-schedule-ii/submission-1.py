class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hm = defaultdict(list)
        for c,p in prerequisites:
            hm[c].append(p)

        path = set()
        visited = set()
        res = []

        def dfs(node):
            if node in path:
                return False
            
            if node in visited:
                return True
            
            path.add(node)
            for preq in hm[node]:
                if not dfs(preq): 
                    return False
            path.remove(node)
            visited.add(node)
            res.append(node)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return res       