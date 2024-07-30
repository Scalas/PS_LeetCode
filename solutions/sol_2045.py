from typing import List


class Solution:
    @staticmethod
    def second_minimum(n: int, edges: List[List[int]], time: int, change: int) -> int:
        visit = [None] * (n + 1)
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        q = [1]
        visit[1] = 0
        cur = 0
        while q:
            if (cur // change) % 2:
                cur += change - cur % change
                continue
            cur += time
            nq = []
            for c in q:
                for nxt in g[c]:
                    if not visit[nxt]:
                        visit[nxt] = cur
                    elif visit[nxt] >= 0:
                        if visit[nxt] != cur:
                            if nxt == n:
                                return cur
                            visit[nxt] = -cur
                    else:
                        continue
                    nq.append(nxt)
            q = nq
