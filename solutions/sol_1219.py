from typing import List


class Solution:
    @staticmethod
    def get_maximum_gold(grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(cr, cc):
            visited[cr][cc] = True
            gold = grid[cr][cc]

            max_left = 0
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                if grid[nr][nc] == 0:
                    continue
                if visited[nr][nc]:
                    continue
                max_left = max(max_left, dfs(nr, nc))
            visited[cr][cc] = False
            return gold + max_left

        answer = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    visited = [[False] * m for _ in range(n)]
                    answer = max(answer, dfs(i, j))
        return answer
