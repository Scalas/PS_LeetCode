from typing import List


class Solution:
    @staticmethod
    def make_connected(n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        g = [[] for _ in range(n)]
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)

        visited = [False] * n

        def dfs(cur):
            visited[cur] = True
            for nxt in g[cur]:
                if visited[nxt]:
                    continue
                dfs(nxt)

        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1

        return count - 1
