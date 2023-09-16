from heapq import heappush, heappop
from typing import List

INF = 10**9


class Solution:
    @staticmethod
    def minimum_effort_path(heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        dp = [[INF] * m for _ in range(n)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = [(0, 0, 0)]
        dp[0][0] = 0
        while q:
            e, r, c = heappop(q)
            if dp[r][c] < e:
                continue
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                ne = max(e, abs(heights[nr][nc] - heights[r][c]))
                if ne < dp[nr][nc]:
                    dp[nr][nc] = ne
                    heappush(q, (ne, nr, nc))
        return dp[-1][-1]
