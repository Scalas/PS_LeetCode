from typing import List


class Solution:
    @staticmethod
    def num_enclaves(grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = [(r, c)]
            grid[r][c] = 0
            while q:
                nq = []
                for cr, cc in q:
                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc
                        if not (0 <= nr < n and 0 <= nc < m):
                            continue
                        if not grid[nr][nc]:
                            continue
                        grid[nr][nc] = 0
                        nq.append((nr, nc))
                q = nq

        for i in range(n):
            if grid[i][0]:
                bfs(i, 0)
            if grid[i][m - 1]:
                bfs(i, m - 1)
        for i in range(m):
            if grid[0][i]:
                bfs(0, i)
            if grid[n - 1][i]:
                bfs(n - 1, i)
        return sum(map(sum, grid))
