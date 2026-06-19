from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def dfs(i):
            for nb in adj[i]:
                if not nb in seen:
                    seen.add(nb)
                    dfs(nb)
                
        
        seen = set()
        ans = 0
        for i in range(n):
            if i not in seen:
                seen.add(i)
                ans+=1
                dfs(i)

        return ans