from typing import List


class Solution:
    @staticmethod
    def cherry_pickup(grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[[-1] * m for _ in range(m)] for _ in range(n)]

        def dfs(row, r1, r2):
            if row + 1 == n:
                return 0

            if dp[row][r1][r2] == -1:
                res = 0
                for nr1 in range(max(0, r1 - 1), min(m, r1 + 2)):
                    for nr2 in range(max(0, r2 - 1), min(m, r2 + 2)):
                        picked = grid[row + 1][nr1] + grid[row + 1][nr2]
                        if nr1 == nr2:
                            picked -= grid[row + 1][nr1]
                        res = max(res, dfs(row + 1, nr1, nr2) + picked)
                dp[row][r1][r2] = res

            return dp[row][r1][r2]

        return dfs(0, 0, m - 1) + grid[0][0] + grid[0][m - 1]
