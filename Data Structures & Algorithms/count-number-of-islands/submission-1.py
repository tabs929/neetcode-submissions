class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        seen = set()
        ans = 0

        def is_valid(r,c):
            return (0<=r<m and 0<=c<n and grid[r][c] == "1" and (r,c) not in seen)

        def dfs(r,c):
            for x,y in directions:
                nr,nc = r+x, c+y
                if is_valid(nr,nc):
                    seen.add((nr,nc))
                    dfs(nr,nc)

        for r in range(m):
            for c in range(n):
                if (r,c) not in seen and grid[r][c] == "1":
                    ans+=1
                    dfs(r,c)
                    seen.add((r,c))
        return ans