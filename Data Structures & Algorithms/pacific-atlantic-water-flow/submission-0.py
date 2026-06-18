class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights),len(heights[0])
        pac ,atl = set(),set()

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c,visit,prevHeight):
            if ((r,c) in visit or
                r<0 or c<0 or 
                r==m or c==n or
                heights[r][c] < prevHeight):
                return

            visit.add((r,c))
            for x,y in directions:
                nr,nc = r+x,c+y
                dfs(nr,nc,visit,heights[r][c])

        for c in range(n):
            dfs(0,c,pac,heights[0][c])
            dfs(m - 1,c, atl,heights[m-1][c])

        for r in range(m):
            dfs(r,0,pac,heights[r][0])
            dfs(r,n-1, atl,heights[r][n-1])

        res = []
        for r in range(m):
            for c in range(n):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res