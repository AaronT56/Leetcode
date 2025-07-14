class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for i in range(n)]

        visit = [False] * n
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        
        return res
            
