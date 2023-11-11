from heapq import heappop, heappush
from typing import List


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.INF = float("inf")
        self.n = n
        self.g = [[] for _ in range(n)]
        for u, v, w in edges:
            self.g[u].append([v, w])

    def add_edge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.g[u].append([v, w])

    def shortest_path(self, node1: int, node2: int) -> int:
        d = [self.INF] * self.n
        d[node1] = 0
        q = [(0, node1)]
        while q:
            dst, cur = heappop(q)
            if d[cur] < dst:
                continue
            for nxt, dist in self.g[cur]:
                ndst = dist + dst
                if ndst < d[nxt]:
                    d[nxt] = ndst
                    heappush(q, (ndst, nxt))
        return d[node2] if d[node2] != self.INF else -1
