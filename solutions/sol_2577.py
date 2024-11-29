from heapq import heappop, heappush
from typing import List


class Solution:
    @staticmethod
    def minimum_time(grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        inf = float("inf")
        min_slots = [[inf] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                res = inf
                for dr, dc in directions:
                    ni, nj = i + dr, j + dc
                    if not (0 <= ni < n and 0 <= nj < m):
                        continue
                    res = min(res, grid[ni][nj])
                min_slots[i][j] = res

        q = [[0, 0, 0]]
        reached_at = [[inf] * m for _ in range(n)]
        reached_at[0][0] = 0
        while q:
            cur_time, cr, cc = heappop(q)
            if reached_at[cr][cc] < cur_time:
                continue
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                nxt_time = cur_time + 1
                if grid[nr][nc] > nxt_time:
                    if min_slots[cr][cc] > nxt_time:
                        continue
                    diff = grid[nr][nc] - cur_time
                    nxt_time = grid[nr][nc] + (1 - diff % 2)
                if nxt_time < reached_at[nr][nc]:
                    reached_at[nr][nc] = nxt_time
                    heappush(q, [nxt_time, nr, nc])

        res = reached_at[n - 1][m - 1]
        return res if res != inf else -1
