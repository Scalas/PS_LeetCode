from typing import List


class Solution:
    @staticmethod
    def count_pairs(n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        visited = [False] * n

        def dfs(cur):
            visited[cur] = True
            res = 1
            for nxt in g[cur]:
                if visited[nxt]:
                    continue
                res += dfs(nxt)
            return res

        clusters = []
        for i in range(n):
            if not visited[i]:
                clusters.append(dfs(i))

        m = len(clusters)
        for i in range(1, m):
            clusters[i] += clusters[i - 1]
        clusters.append(0)

        answer = 0
        for i in range(m - 1):
            cur = clusters[i] - clusters[i - 1]
            remain = clusters[m - 1] - clusters[i]
            answer += cur * remain
        return answer
