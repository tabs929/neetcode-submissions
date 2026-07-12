class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        maxArea = 0
        visit = set()

        def isValid(r,c):
            return (0<=r<m and 0<=c<n and grid[r][c]==1 and (r,c) not in visit)

        def dfs(r,c):
            area = 1
            for x,y in directions:
                nr,nc = r+x,c+y
                if isValid(nr,nc):
                    visit.add((nr,nc))
                    area+=dfs(nr,nc)
            return area
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 :
                    visit.add((r,c))
                    maxArea = max(maxArea,dfs(r,c))
        return maxArea