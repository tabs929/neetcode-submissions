class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid),len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        dist = 0
        q = deque()

        def isValid(r,c):
            return (0<=r<m and 0<=c<n and grid[r][c]!= -1 and (r,c) not in visited)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                visited.add((r,c))
                for x,y in directions:
                    nr,nc = r+x,c+y
                    if isValid(nr,nc):
                        visited.add((nr,nc))
                        q.append((nr,nc))
            dist+=1