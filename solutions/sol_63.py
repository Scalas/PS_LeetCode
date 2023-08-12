from typing import List


class Solution:
    @staticmethod
    def unique_paths_with_obstacles(obstacle_grid: List[List[int]]) -> int:
        n, m = len(obstacle_grid), len(obstacle_grid[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(m):
            if obstacle_grid[0][i]:
                break
            dp[0][i] = 1
        for i in range(n):
            if obstacle_grid[i][0]:
                break
            dp[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                if obstacle_grid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n - 1][m - 1]
