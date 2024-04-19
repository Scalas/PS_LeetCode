from typing import List


class Solution:
    @staticmethod
    def num_islands(grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(cr, cc):
            grid[cr][cc] = "0"
            for dr, dc in direction:
                nr, nc = cr + dr, cc + dc
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                if grid[nr][nc] == "0":
                    continue
                dfs(nr, nc)

        answer = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "0":
                    continue
                answer += 1
                dfs(i, j)
        return answer
