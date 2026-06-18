class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def is_valid(row,col):
            return (0<=row<m and 
            0<=col<n and 
            grid[row][col] == "1" 
            and (row,col) not in seen)

        def dfs(r,c):
            for x,y in directions:
                nr,nc = r+x,c+y
                if is_valid(nr,nc):
                    seen.add((nr,nc))
                    dfs(nr,nc)
        
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        m,n = len(grid),len(grid[0])
        seen = set()
        ans = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r,c) not in seen:
                    ans+=1
                    seen.add((r,c))
                    dfs(r,c)

        return ans