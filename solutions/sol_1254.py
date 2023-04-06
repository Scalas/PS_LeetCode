from typing import List


class Solution:
    @staticmethod
    def closed_island(grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = [(r, c)]
            visited[r][c] = True
            while q:
                nq = []
                for cr, cc in q:
                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc
                        if not (0 <= nr < n and 0 <= nc < m):
                            continue
                        if grid[nr][nc]:
                            continue
                        if visited[nr][nc]:
                            continue
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                q = nq

        for i in range(n):
            if not grid[i][0] and not visited[i][0]:
                bfs(i, 0)
            if not grid[i][m - 1] and not visited[i][m - 1]:
                bfs(i, m - 1)
        for i in range(m):
            if not grid[0][i] and not visited[0][i]:
                bfs(0, i)
            if not grid[n - 1][i] and not visited[n - 1][i]:
                bfs(n - 1, i)

        answer = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if grid[i][j]:
                    continue
                if visited[i][j]:
                    continue
                bfs(i, j)
                answer += 1
        return answer
