from typing import List


class Solution:
    @staticmethod
    def min_score(n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for u, v, w in roads:
            g[u].append(v)
            g[v].append(u)
        q = [1]
        visited = [False] * (n + 1)
        visited[1] = True

        while q:
            nq = []
            for cur in q:
                for nxt in g[cur]:
                    if visited[nxt]:
                        continue
                    visited[nxt] = True
                    nq.append(nxt)
            q = nq

        min_road = 10 ** 5
        for u, v, w in roads:
            if visited[u] and visited[v]:
                min_road = min(min_road, w)
        return min_road
