from typing import List

INF = 10**9


class Solution:
    @staticmethod
    def shortest_alternating_paths(
        n: int, red_edges: List[List[int]], blue_edges: List[List[int]]
    ) -> List[int]:
        dp = [[INF, INF] for _ in range(n)]
        rg = [[] for _ in range(n)]
        bg = [[] for _ in range(n)]
        for u, v in red_edges:
            rg[u].append(v)
        for u, v in blue_edges:
            bg[u].append(v)
        q = [(0, 0), (0, 1)]
        dp[0] = [0, 0]
        while q:
            nq = []
            for cur, pre in q:
                if pre == 1:
                    for nxt in rg[cur]:
                        if dp[nxt][0] != INF:
                            continue
                        dp[nxt][0] = dp[cur][1] + 1
                        nq.append((nxt, 0))
                else:
                    for nxt in bg[cur]:
                        if dp[nxt][1] != INF:
                            continue
                        dp[nxt][1] = dp[cur][0] + 1
                        nq.append((nxt, 1))
            q = nq
        sp = [min(dp[i]) for i in range(n)]
        for i in range(n):
            if sp[i] == INF:
                sp[i] = -1
        return sp
