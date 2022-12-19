from typing import List


class Solution:
    @staticmethod
    def valid_path(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u - 1].append(v - 1)
            g[v - 1].append(u - 1)

        if source == destination:
            return True

        q = [source - 1]
        visited = [False] * n
        while q:
            nq = []
            for cur in q:
                for nxt in g[cur]:
                    if nxt == destination - 1:
                        return True
                    if not visited[nxt]:
                        visited[nxt] = True
                        nq.append(nxt)
            q = nq
        return False
