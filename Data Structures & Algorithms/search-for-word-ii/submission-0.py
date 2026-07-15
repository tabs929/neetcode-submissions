class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def add_word(self,word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add_word(w)

        m,n = len(board),len(board[0])
        res,visit = set(),set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c,node,word):
            if (
                r < 0 or
                r >= m or
                c < 0 or
                c >= n or
                (r, c) in visit or
                board[r][c] not in node.children
            ):
                return

            visit.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord:
                res.add(word)
                node.isWord = False

            for dr, dc in directions:
                dfs(r + dr, c + dc, node, word)

            visit.remove((r, c))

        for r in range(m):
            for c in range(n):
                dfs(r,c,root,"")

        return list(res)