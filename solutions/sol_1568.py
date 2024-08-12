from typing import List


class Solution:
    @staticmethod
    def min_days(grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def check(sr, sc):
            if 0 <= sr < n and 0 <= sc < m:
                grid[sr][sc] = 0
            visited = [[False] * m for _ in range(n)]
            count = 0
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 0 or visited[i][j]:
                        continue
                    count += 1
                    visited[i][j] = True
                    q = [[i, j]]
                    while q:
                        nq = []
                        for cr, cc in q:
                            for dr, dc in directions:
                                nr, nc = cr + dr, cc + dc
                                if not (0 <= nr < n and 0 <= nc < m):
                                    continue
                                if grid[nr][nc] == 0:
                                    continue
                                if visited[nr][nc]:
                                    continue
                                visited[nr][nc] = True
                                nq.append([nr, nc])
                        q = nq
            if 0 <= sr < n and 0 <= sc < m:
                grid[sr][sc] = 1
            return count != 1

        if check(-1, -1):
            return 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and check(i, j):
                    return 1
        return 2
