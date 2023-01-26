from typing import List
INF = 10 ** 9


class Solution:
    @staticmethod
    def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, d in flights:
            g[u].append((v, d))
        q = [(src, 0)]
        cnt = k + 1
        visited = [INF] * n
        while q and cnt:
            cnt -= 1
            nq = []
            for cur, dist in q:
                for nxt, ndist in g[cur]:
                    ndist += dist
                    if ndist >= visited[nxt]:
                        continue
                    if nxt != dst:
                        nq.append((nxt, ndist))
                    visited[nxt] = ndist
            q = nq
        answer = visited[dst]
        return answer if answer != INF else -1
