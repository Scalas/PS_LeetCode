from typing import List


class Solution:
    @staticmethod
    def unique_paths_3(grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        answer = 0
        n, m = len(grid), len(grid[0])
        sr, sc = 0, 0
        er, ec = 0, 0
        tc = n * m
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    sr, sc = i, j
                elif grid[i][j] == 2:
                    er, ec = i, j
                elif grid[i][j] == -1:
                    tc -= 1

        visited = [[False] * m for _ in range(n)]
        vc = 0

        def dfs(r, c):
            nonlocal answer, vc
            if r == er and c == ec:
                if vc == tc:
                    answer += 1
                return
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                if visited[nr][nc]:
                    continue
                if grid[nr][nc] == -1:
                    continue
                visited[nr][nc] = True
                vc += 1
                dfs(nr, nc)
                vc -= 1
                visited[nr][nc] = False

        visited[sr][sc] = True
        vc += 1
        dfs(sr, sc)

        return answer
