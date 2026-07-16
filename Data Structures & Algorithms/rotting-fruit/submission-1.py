class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        m,n = len(grid),len(grid[0])
        direc = [[1,0],[-1,0],[0,1],[0,-1]]
        fresh = 0;mins=0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        def isValid(r,c):
            return (0<=r<m and 0<=c<n and grid[r][c] == 1)
        
        while q and fresh > 0:
            length = len(q)
            for _ in range(length):
                r,c = q.popleft()

                for dr,dc in direc:
                    nr,nc = r+dr,c+dc
                    if isValid(nr,nc):
                        grid[nr][nc] = 2
                        fresh-=1
                        q.append((nr,nc))
            mins+=1
        return mins if fresh == 0 else -1