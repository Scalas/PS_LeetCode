from typing import List


class Solution:
    @staticmethod
    def maximal_network_rank(n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for i in range(len(roads)):
            u, v = roads[i]
            g[u].append(i)
            g[v].append(i)

        answer = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                answer = max(answer, len(set(g[i]) | set(g[j])))
        return answer
