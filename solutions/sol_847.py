from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def shortest_path_length(graph: List[List[int]]) -> int:
        n = len(graph)
        t = 2**n - 1
        INF = 2 * n

        dp = [[INF] * (t + 1) for _ in range(n)]

        q = []
        for i in range(n):
            q.append([0, i, 1 << i])
            dp[i][1 << i] = 0

        while q:
            c, cur, visit = heappop(q)
            if dp[cur][visit] < c:
                continue
            for nxt in graph[cur]:
                nc, nvisit = c + 1, visit | (1 << nxt)
                if dp[nxt][nvisit] <= nc:
                    continue
                dp[nxt][nvisit] = nc
                heappush(q, [nc, nxt, nvisit])

        return min([dp[i][t] for i in range(n)])
