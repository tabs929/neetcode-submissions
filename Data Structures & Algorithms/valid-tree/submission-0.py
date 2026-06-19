from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        seen = set()
        def dfs(node ,prev):
            if node in seen:
                return False
            
            seen.add(node)
            for nb in adj[node]:
                if nb == prev:
                    continue
                if not dfs(nb, node):
                    return False
                
            return True
        
        return (dfs(0,-1) and len(seen) == n)