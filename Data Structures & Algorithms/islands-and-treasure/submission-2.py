class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid),len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque(); INF = 2147483647

        def isValid(r,c):
            return (0<=r<m and 0<=c<n and grid[r][c] == INF)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            r,c = q.popleft()
            for x,y in directions:
                nr,nc = r+x,c+y
                if isValid(nr,nc):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))