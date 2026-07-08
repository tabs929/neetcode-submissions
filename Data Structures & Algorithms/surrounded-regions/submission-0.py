class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board) , len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def isValid(r,c):
            return (0<=r<m and 0<=c<n and board[r][c] == "O")

        def dfs(r,c):
            if not isValid(r,c):
                return
            board[r][c] = "T"
            for x,y in directions:
                dfs(r+x,c+y)
            
        for r in range(m):
            for c in range(n):
                if board[r][c] =="O" and (r in [0,m-1] or c in [0,n-1]):
                    dfs(r,c)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] =="O":
                    board[r][c] = "X"
        
        for r in range(m):
            for c in range(n):
                if board[r][c] =="T":
                    board[r][c] = "O"