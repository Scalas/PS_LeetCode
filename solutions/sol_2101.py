from math import sqrt
from typing import List


class Solution:
    @staticmethod
    def maximum_detonation(bombs: List[List[int]]) -> int:
        n = len(bombs)

        g = [[] for _ in range(n)]

        u = [-1] * n
        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if d <= r1:
                    g[i].append(j)

        def dfs(cur):
            res = 1
            visited[cur] = True
            for nxt in g[cur]:
                if visited[nxt]:
                    continue
                res += dfs(nxt)
            return res

        answer = 0
        for i in range(n):
            visited = [False] * n
            answer = max(answer, dfs(i))
        return answer
