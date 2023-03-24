from typing import List


class Solution:
    @staticmethod
    def min_reorder(n: int, connections: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in connections:
            g[u].append((v, 1))
            g[v].append((u, 0))

        visited = [False] * n
        q = [0]
        visited[0] = True
        answer = 0
        while q:
            nq = []
            for cur in q:
                for nxt, dist in g[cur]:
                    if visited[nxt]:
                        continue
                    visited[nxt] = True
                    nq.append(nxt)
                    answer += dist
            q = nq
        return answer
