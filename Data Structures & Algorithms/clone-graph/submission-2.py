class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for nb in node.neighbors:
                copy.neighbors.append(dfs(nb))

            return oldToNew[node]

        return dfs(node) if node else None