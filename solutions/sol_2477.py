from math import ceil
from typing import List


class Solution:
    @staticmethod
    def minimum_fuel_cost(roads: List[List[int]], seats: int) -> int:
        if not roads:
            return 0
        n = max(map(max, roads)) + 1
        g = [[] for _ in range(n)]
        for u, v in roads:
            g[u].append(v)
            g[v].append(u)

        visited = [False] * n

        def dfs(cur):
            visited[cur] = True
            cnt, cost = 1, 0
            for nxt in g[cur]:
                if visited[nxt]:
                    continue
                scnt, scost = dfs(nxt)
                cnt += scnt
                cost += scost
                cost += ceil(scnt / seats)
            return cnt, cost

        return dfs(0)[1]
