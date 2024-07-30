from typing import List


class Solution:
    @staticmethod
    def find_the_city(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        inf = float("inf")
        adj = [[inf] * n for _ in range(n)]
        for i in range(n):
            adj[i][i] = 0
        for u, v, w in edges:
            adj[u][v] = adj[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adj[j][i] = adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
        answer, min_neighbor = -1, inf
        for i in range(n - 1, -1, -1):
            neighbor = 0
            for j in range(n):
                if i == j:
                    continue
                if adj[i][j] <= distanceThreshold:
                    neighbor += 1
            if neighbor < min_neighbor:
                answer, min_neighbor = i, neighbor
        return answer
