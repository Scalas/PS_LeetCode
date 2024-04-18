from typing import List


class Solution:
    @staticmethod
    def island_perimeter(grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[False] * m for _ in range(n)]

        def dfs(cr, cc):
            visited[cr][cc] = True
            res = 0
            for dr, dc in direction:
                nr, nc = cr + dr, cc + dc
                if not (0 <= nr < n and 0 <= nc < m):
                    res += 1
                    continue
                if grid[nr][nc] == 0:
                    res += 1
                    continue
                if visited[nr][nc]:
                    continue
                res += dfs(nr, nc)
            return res

        answer = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                if visited[i][j]:
                    continue
                answer += dfs(i, j)
        return answer
