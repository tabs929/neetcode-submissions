from collections import defaultdict

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        direc = [[1,0],[-1,0],[0,1],[0,-1]]
        rotten = []
        fresh,mins= 0,0

        def isValid(r,c):
            return (0<=r<m and 0<=c<n and grid[r][c] == 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1
        
        while rotten and fresh>0:
            mins+=1
            curr = []
            for r,c in rotten:
                for x,y in direc:
                    nr,nc = r+x,c+y
                    if isValid(nr,nc):
                        grid[nr][nc] = 2
                        fresh-=1
                        curr.append((nr,nc))
                    if fresh == 0:
                        return mins
            rotten = curr

        return mins if fresh==0 else -1
        