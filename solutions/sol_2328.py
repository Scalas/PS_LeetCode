from typing import List


class Solution:
    @staticmethod
    def count_paths(grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[-1] * m for _ in range(n)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        mod = 10 ** 9 + 7

        def dfs(r, c):
            if dp[r][c] == -1:
                res = 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < n and 0 <= nc < m):
                        continue
                    if grid[nr][nc] <= grid[r][c]:
                        continue
                    res = (res + dfs(nr, nc)) % mod
                dp[r][c] = res
            return dp[r][c]

        answer = 0
        for i in range(n):
            for j in range(m):
                answer = (answer + dfs(i, j)) % mod
        return answer
