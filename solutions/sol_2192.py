from typing import List


class Solution:
    @staticmethod
    def get_ancestors(n: int, edges: List[List[int]]) -> List[List[int]]:
        g: List[List[int]] = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
        ancestors = [[] for _ in range(n)]

        def bfs(start):
            q = [start]
            visited = [False] * n
            while q:
                nq = []
                for cur in q:
                    for nxt in g[cur]:
                        if visited[nxt]:
                            continue
                        visited[nxt] = True
                        ancestors[nxt].append(start)
                        nq.append(nxt)
                q = nq

        for i in range(n):
            bfs(i)
        return ancestors
