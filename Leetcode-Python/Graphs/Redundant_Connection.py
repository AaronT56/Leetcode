class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        startCycle = -1
        n = len(edges)
        adj = [[] for i in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        cycle = set()
        visit = [False] * (n - 1)

        def dfs(node, parent):
            nonlocal startCycle
            if visit[node]:
                startCycle = node
                return True
            
            visit[node] = True
            # So because this is a undirected graph, the node we just came from, will have
            # the parent as one of its elements in the adj list. So in order to not detect
            # fake cycles (if we didn't have this every node would be considered a cycle)
            # we keep iterating through the adjacency matrix making sure to skip the parent
            # each time.
            for nei in adj[node]:
                if nei == parent:
                    continue
                
                # So first key thing, remember we are backtracking. So we go this line
                # dfs(nei, node) will keep creating new calls, until we finally get a
                # return True from the above line. Then, we will backtrack until we get
                # startCycle = -1 and return False. The key is to remember, that this
                # dfs function will be called until it hits True, then work backwards
                # appending to the cycle each time until it returns falls. And then 
                # we will have a set with all members of the cycle! We will get false
                # once we return to the first node in the cycle.
                if dfs(nei, node):
                    if startCycle != -1:
                        cycle.add(node)
                    if node == startCycle:
                        startCycle = -1
                    return True
            return False
    
        dfs(-1, 1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        return []